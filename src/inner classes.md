title: Nested Classes
category: Technical
description: Learn about nested classes in Java and why you should start using them.
date: 2013-09-09 3:3:3

<h2>What Are They?</h2>
<p>Nested and inner classes are synonomous depending on where you read about them.  There are two types of inner classes: <strong>static and non-static</strong>.</p>

<p>Non-static inner classes are treated just like a normal member variable in a class and have full access to other member variables and methods within the enclosing class. </p> 

<p>A static inner class does not have direct access to other members or methods of the enclosing class.  Nested classes can also be declared as public, private, protected, ad package private.</p>

<h2>Example</h2>
<p></p>
	:::java
	public interface Bark {
		public void makeSound();
	}

	public class Dog {
		private Bark mBark;
		private Toy mToy;
		public Dog() {
			mBark = new BarkImpl();
			mToy = new Toy("Squeaky");
			//Note that if used outside of Dog would need to be Dog.Toy()
		}

		//Private non-static inner class
		//Don't need to pollute package with with class that is used only in Dog
		private class BarkImpl implements Bark {
			public void makeSound() {
				System.out.println("Woof.");
			}
		}

		//Static inner class that behaves like package level class
		//Strong relationship between Dog and Toy so makes sense to nest
		public static class Toy {
			private String name;
			public Toy(String name) {
				this.name = name;
			}
		}
	} 

<p></p>

<h2>So What's The Point?</h2>
<p>The point of using inner classes is increased encapsulation, a topic that I have mentioned many times.  If a class is designed specifically for use with another class, then it makes sense to group them together.  Not only does this make everything more readable, but it's easier to maintain since it is in one location.</p>

<p>Always consider a new programmer trying to work with your code.  When I work with new code, I like to inspect what is in each package to try and get a feel for everything.  If packages were bloated with all the helper classes used by the core classes then it would take a long time for me to figure out where to start.  Classes exposed at the package level should be classes that you want another developer to interact with.</p>

<h2>Static Inner Classes</h2>
<p>A static inner class is essentially treated exactly like a top-level class in a package.  The only difference is its location and how it is called.  To call a static nested class, you have to do it like this:</p>

	:::java
	OuterClass.StaticInnerClass nested = new OuterClass.StaticNestedClass();

<p>Usually whatever IDE you are using will help take care of this for you, but it's not hard to remember.</p>

<h2>Non-Static Inner Classes</h2>
<p>These can also be created outside of the enclosing class, but I don't encourage it very often. If you need to use a non-static inner class often outside of its enclosing class, I would suggest making it static or not an inner class.  They can be instantiated like so:</p>

	:::java
	OuterClass outerObject = new OuterClass();
	OuterClass.InnerClass nested = outerObject.new InnerClass();

<p>Note that you need to already have instantiated an OuterClass object to instantiate a non-static inner class because it doesn't exist without an instance of its enclosing class.</p>

<h2>Good Uses</h2>
<p>For static inner classes, I like to use them when I want to show a clear relation to the enclosing class.  Consider this example found in the JDK: <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Map.Entry.html">Map.Entry</a>.  Technically it is an interface, but the same encapsulation principles apply.</p>

<p>For non-static inner classes, I don't generally use them with the public access modifier.  I do use them very often with the private access modifier.  For example, when creating subclasses or interface implementations that are only relevant to the enclosing class, and used often enough where I don't want to make construct them in an anonymous class.</p>

<h2>Read More!</h2>
<p>I would recommend reading through the entire <a href="http://docs.oracle.com/javase/tutorial/java/javaOO/index.html">Java tutorial</a> on all sorts of classes.  It also doesn't hurt to read the section on <a href="http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html">Shadowing</a>, which I did not cover here and involves handling scope issues.
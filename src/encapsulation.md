layout: default_post
title: The Basics of Encapsulation
category: Technical
date: 2013-04-04 4:4:4
description: Learn the basics of Encapsulation, one of the key Object Oriented Programming concepts.

<h2>Encapsulation</h2>
<p>Encapsulation is a key concept to learn because it helps maintain separation for different sections of your code.  Having code protected from other code can be very useful for debugging your program.  It also aids in readability where another programmer can quickly figure out how to interact with your code.</p>

<p>Take the following example:</p>
    :::java
    public class Employee {
        //Member variables
        private String name;
        private int age;
        private int weeklyPay;
        private double taxRate;

        public Employee(String name, int age, int weeklyPay, double taxRate) {
            this.name = name;
            this.age = age;
            this.weeklyPay = weeklyPay;
            this.taxRate = taxRate;
        }

        private double calcTakeHome() {
            return weeklyPay * (1-taxRate); //Subtract taxes
        }

        public double getYearlySalary() {
            return calcTakeHome() * 52; //52 weeks in a year
        }
    }

<p>Lets do some review first.  A public constructor, method, or variable is exposed to the world.  Generally, you make something public if you want other programmers to interact with it.  The exception to this is member variables, where you usually create get/set methods for direct interaction.  With that in mind, another programmer could come and use my class like so:</p>

    :::java
    Employee bob = new Employee("Bob",42,1000,.07);
    double salary = bob.getYearlySalary();

<p>This would compile fine.  So in contrast, what is a private constructor, method, or variable?  Something is made private when you <strong>don't</strong> want other programmers to interact with it.  For all intents and purposes, it doesn't even exist to them.  If an API was created for my Employee class, the method <code>calcTakeHome()</code> wouldn't be mentioned and neither would my member variables because they are private.  The only way another programmer could know about those methods and variables would be if they looked directly at my source code or used reflection.  Take a look at this code:</p>

    :::java
    Employee bob = new Employee("Bob",42,1000,.07);
    double takeHome = bob.calcTakeHome(); //Compile error because private

<p>This code will give you a compile error.  The reason is that Java detected me trying to use a private method.  Private methods and variables are considered internal to a class, often called class helpers.  I could certainly write the method <code>getYearlySalary()</code> like this:</p>

    :::java
    public double getYearlySalary() {
        return weeklyPay * (1-taxRate) * 52; //52 weeks in a year
    }

<p>And not even use the <code>calcTakeHome()</code> method, but it is a lot simpler if I break it up into multiple methods.  So think of private methods as helpers to writing your public methods that other programmers will use.</p>

<h2>Why is this helpful?</h2>
<p>Programmers have to read through lots of code every day, and most of the code will be written by other programmers.  To cut down on this time helper methods and variables are hidden from them so that the programmer only sees what they can actually interact with in the class.  When I wrote the Employee class, I deemed that it was only necessary for somebody to calculate an Employee's yearly salary and not their weekly take home pay which is why the two methods are public and private respectively.  Someone using my class will then see all the public constructors, methods, and variables that I have declared and be able to figure out how to use my class.</p>

<p>This also falls in line with the OOP principle <strong>DRY</strong>, short for Don't Repeat Yourself.  If you find yourself repeating a lot of code within your class it makes sense to extract that into a private method.  This way if you need to make any changes there is only one place to modify code.  Other programmers will not care about this method which is why you don't need to make it public, since it is only helping you.</p>

<h2>Visibility</h2>
<p>The technical term for this is visibility.  This is one of the major Object Oriented Programming advantages and there are lots more to it than this, but this is a good primer for you to start!  There are four different types of visibility (public, private, protected, default) in Java which you can read more about here: <a href="http://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html">Controlling Access to Members of a Class</a></p>
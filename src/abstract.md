layout: default_post
title: The Abstract Keyword
category: Technical
date: 2013-04-04 4:4:5
description: Learn how to properly use the abstract keyword.

<p>This is a long tutorial so you may have to read everything through a couple times. :)</p>
<h2>What is an abstract class or method?</h2>
<p>A class that is abstract is one that cannot be instantiated, only subclassed, which means that trying to create an object for an abstract class will generate a compiler error.  An abstract class can contain implementation for its methods as well as variables.</p>  

<p>A common interview question is to explain the difference between an interface and an abstract class.  The difference is that an interface cannot contain any implementation of its methods, only signatures.  Classes can also implement as many interfaces as they would like, while only one abstract class can be extended at a time.  One caveat is that static methods or variables <strong>will</strong> use the abstract class name to be called if they are declared in the abstract class.  For example:</p>

    :::java
    AbstractClass shouldFail = new AbstractClass(); //error
    AbstractClass.staticMethod(); //runs fine
<p></p>
<h2>Why You Should Use Them!</h2>
<p>One of the main OOP principles is DRY, short for <strong>Don't Repeat Yourself</strong>.  If you find code that is common in many classes, it probably means you can create a super class.  The benefits of an abstract class compared to a normal super class is that you force implementation into a subclass -- because they cannot be instantiated -- and can provide unimplemented behavior with abstract methods.  If you need to change something in the future that affects all implementations, you have one central place to make that change.</p>

<h2>Notation</h2>
<p>Here are some examples of how an abstract class and method can be created:</p>

    :::java
    public abstract class Table {
        String name = "table";
        String values;

        public void setTableName(String name) {
            this.name = name;
        }

        public void setValues(String values) {
            this.values = values;
        }

        public JSONObject toJSON() {
            return new JSONObject(values);
        }

        public abstract void displayTable();
    }

    public class SpecificTable extends Table {
        public void displayTable() {
            System.out.println("Specific " + name);
        }
    }

    public class GeneralTable extends Table {
        public void displayTable() {
            System.out.println("General " + name);
        }
    }

<p>As you can see, the method <code>displayTable()</code> is an abstract method.  It cannot be created with any implementation and can only be declared within an abstract class, or else you will run into compile issues.</p>

<p>Now lets try running that with this code:</p>

    :::java
    SpecificTable specific = new SpecificTable();
    GeneralTable general = new GeneralTable();
    specific.displayTable();
    general.displayTable();
    specific.setTableName("tables"); //change the name
    specific.displayTable();


<p>This will output the following:</p>
    :::java
    Specific table
    General table
    Specific tables

<p>In this example, <code>SpecificTable</code> and <code>GeneralTable</code> are the subclass implementations of Table.  Each has a different implementation of the <code>displayTable()</code> method, and you can see that they both have some methods in common such as <code>setTableName()</code>.</p>

<h2>Enum trick</h2>
<p>Another good thing to know is that an <code>Enum</code> can also contain abstract methods.  If you declare an abstract method in an <code>Enum</code>, then each value will have to implement that method like this:</p>

    :::java
    public enum Algorithm {
        SRTF {
            public String getName() {return "Shortest run-time first";}
        },
        FCFS {
            public String getName() {return "First come first serve";}
        },
        RR {
            public String getName() {return "Round robin";}
        };
        public abstract String getName();
    }

<p>That code can then be called like so:</p>
    :::java
    Algorithm fcfs = Algorithm.FCFS;
    String name = fcfs.getName();
<p></p>
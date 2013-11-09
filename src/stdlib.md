layout: default_post
title: Know Your Standard Libraries
category: Technical
date: 2013-11-09 4:4:5
description: Learn why it is best to learn and be familiar with the standard libraries available in your language.

<h2>Why?</h2>
<p>Many new programmers try to reinvent the wheel on everything they do.  What many don't realize is that some languages have been around for decades!  Smart programmers have figured out solutions to many of the problems that they are likely to face.  This is one of the reasons why I love Java.  It's standard library is huge and can solve most problems I have without making me write lots of code.</p>

<p>For Java, I recommend people to poke around through the awesome Javadocs available, found <a href="http://docs.oracle.com/javase/7/docs/api/">here</a>.  This may look daunting at first.  Here's some packages that you SHOULD look over:</p>

<ul>
<li><code>java.io</code>: Used for I/O operations.</li>
<li><code>java.lang.*</code>: Fundamental classes to the Java language.</li>
<li><code>java.math</code>: Useful math classes.</li>
<li><code>java.net</code>: Stuff for network operations.</li>
<li><code>java.util.*</code>: Contains awesome utility classes and home of the Concurrent libraries.  Home of the Collections library too.</li>
</ul>

<h2>Case study</h2>
<p>You are in an interview and given a list of objects.  The list contains simple <code>Person</code> POJO's (Plain Old Java Object) that contains data such as age, weight, etc.  They want you to sort this list and return it.</p>

<p>Now, this doesn't seem too bad.  You remember learning about some basic sorts in your algorithms class.  Quicksort and Mergesort are two of the best sorts, but you might have some trouble implementing them on the spot during an interview.  You decide to play it safe and go with Bubble sort.  After thirty grueling minutes, you finally think you've implemented your sort.</p>

<p>So how'd you do?  Sorry to break it to you, but BAD!</p>

<p>Sorting is one thing that is tricky to get correct.  There are lots of ways to introduce subtle bugs that will only break on a certain input.  It's best to leave the implementation to lanaguage designers and researchers.  The first words out of your mouth after hearing they want you to sort a list should be "Can I use the standard library?"</p>

<h2>Using the standard lib</h2>
<p>Here's how simple that sorting problem turns into when using the standard library:</p>

    :::java
    /**
     * Sorts in-place the given list, smallest age first
     * @param list List to sort.
     */
    public void sortByAge(List<Person> list) {
        Comparator<Person> ageComp = new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                return o1.getAge() - o2.getAge();
            }
        };
        Collections.sort(list, ageComp);
    }

<p>Using our knowledge of Java Collections, we were able to sort this using a <code>Comparator</code> with a very fast Timsort algorithm.  We didn't have to implement any part of the sorting which cuts down on the number of potential mistakes we can make, and our Bubble sort only ran in $O(n^2)$ time.  Learn your standard libraries!</p>
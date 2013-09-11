layout: default_post
title: How to Find the Middle of a Linked List
category: Technical
date: 2013-03-10 8:8:8
description: Learn how to find the middle of a Linked List very efficiently.

<h2>The Question</h2>
<p>Given a root node to a linked list, create a method that will return the middle element of the linked list.  Do this without any knowledge of the size of the list.</p>

<h2>The Approach</h2>
<p>This is really more of a "gotcha" question that interviewers commonly ask to see how the interviewee handles having common functionality and API's removed.  It would be trivial to implement this if we were allowed to use the <code>.size()</code> method of a list, but that is forbidden.  Instead, we will have to think a little outside the box.</p>

<p>The first time I tried this problem, I thought of iterating to the end of the list, counting the number of iterations, and then doing half of that the next time.  Even though this doesn't explicitly use the <code>.size()</code> method, it's still considered breaking the rules of the question so don't make this mistake!  Instead think of what is happening within the problem.  We have a list of size <code>n</code>, and we want to return the element at position <code>n/2</code>.  That means the end of the list is growing twice as fast as the middle, hmm...</p>

<h2>The Solution</h2>
<p>So if you haven't thought of it already, think about this.  Create two pointers <code>a</code> and <code>b</code> to the root node that was passed in.  If <code>a</code> is supposed to represent the middle element, how can we have that be half the distance down the list as pointer <code>b</code>?  Very simply actually, just iterate pointer <code>b</code> twice as fast as pointer <code>a</code>.  When pointer <code>b</code> reaches the end, then you can just return pointer <code>a</code>!  Here's an implementation:</p>

    :::java
    /**
     * Returns the middle node of a list.
     * @param root The root node of the list.
     * @return The middle node.
     */
    public Node findMiddle(Node root)
    {
      Node a = root;
      Node b = root;
      while(b.getNext() != null)
      {
        b = b.getNext();
        if(b.getNext() == null)
          return a;
        else
        {
          a = a.getNext();
          b = b.getNext();
        }
      }
      return a;
    }

<p>This code works by iterating <code>Node b</code> twice as much as <code>Node a</code>.  We have to be careful when handling <code>Node b</code>.  If <code>b</code> reaches the end of the list and becomes null, and then we try to use <code>.getNext()</code> on that null object, a <code>NullPointerException</code> will be thrown.</p>
<p>This algorithm will run in <code>O(n)</code> time because it only has to run for the length of the list.</p>
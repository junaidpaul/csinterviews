layout: default_post
title: Create a Queue With Stacks
category: Technical
date: 2013-04-05 4:4:4
description: Learn how to implement a queue by using two stacks.

<h2>What is a queue?</h2>
<p>If you have forgotten, a queue is a data structure that handles objects on a FIFO (first in, first out) basis.  The first element added will also be the first element removed.  Think of it like a queue for checking out at a store.  The person who is first in line will be the next to check out.</p>

<h2>What is a stack?</h2>
<p>A stack is different because it handles objects on a FILO (first in, last out) basis.  Think of it like a stack of cards.  The first card put down will be the last card removed if you are pulling from the top.</p>

<h2>The approach</h2>
<p>The idea here is that we will use two stacks.  One will be used for handling objects being pushed onto the queue.  The other will be used for handling polling (removing) objects from the queue.  Note that due to laziness I did not create this using generics, since that is beyond the scope of this tutorial.  For now the queue will accept the <code>Object</code> type.</p>

    :::java
    public class Queue {
      
      Stack<Object> incoming = new Stack<Object>();
      Stack<Object> outgoing = new Stack<Object>();

      //Enqueues an object to the queue
      public void push(Object o) {
        incoming.push(o);
      }

      //Removes the first object from the queue, null if empty
      public Object poll() {
        //If the outgoing stack isn't empty, then return an object from it
        if(outgoing.isEmpty() == false)
          return outgoing.pop();
        
        //Otherwise we need to push the incoming stack into the outgoing stack
        while(incoming.isEmpty() == false) {
          outgoing.push(incoming.pop());
        }
        
        //Now try returning again
        return outgoing.pop();
      }

      //Returns the size of the Queue
      public int size() {
        return incoming.size() + outgoing.size();
      }

      //Returns if the Queue is empty
      public boolean isEmpty() {
        return size() == 0;
      }

    }

<p></p>

<h2>Explanation</h2>
<p>The key thing here is how we have an incoming and outgoing stack.  Objects pushed to the queue will be added to just the incoming stack.  When the queue is polled, it will first see if the outgoing stack already has something in it.  If nothing is there, then it will try to dump the incoming stack into the outgoing stack.  To make sense of this, look at this diagram:</p>

<img src="/static/images/stack.png">

<p>Once the incoming stack is pushed onto the outgoing stack, the outgoing stack has a FIFO ordering when popped as you can see in the diagram.</p>

<p>The other methods that I included such as <code>size()</code> and <code>isEmpty()</code> simply add up the size of both stacks within queue.  And there you have it!</p>
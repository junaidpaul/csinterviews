layout: default_post
title: How to Reverse a Singly-linked List
category: Technical
date: 2013-03-10 6:6:6
description: Learn how to reverse a Singly-Linked List, a very common interview question!

<h2>The Question</h2>
<p>Your interviewer draws a linked list on the whiteboard that looks like this:</p>

<img src="/static/images/linkedlist-300x58.png" alt="linkedlist" width="300" height="58" />

<p>Where the boxes represent a Node class and the number inside represents an integer value.  Given this, you must create a function that takes in a Node for a parameter, reverses the linked list, and then returns the new root value of the list.  For example, the new list may look like:</p>

<img src="/static/images/linkedlist2-300x55.png" alt="linkedlist2" width="300" height="55" />

<p>And the returned Node would hold an integer value 5.</p>

<h2>The Naive Approach</h2>
<p>The tricky part to this question is that the Node list is singly-linked.  The first thing to mind may be something like this:</p>

<ul>
	<li>Loop until next pointer is null (end of list reached) and store last Node value</li>
	<li>Loop until next pointer equals last Node stored</li>
	<li>Set next pointer from stored Node value to current Node value</li>
	<li>Set last stored Node value to current Node</li>
	<li>Repeat for rest of nodes</li>
</ul>

<p>This method will work, but it is very wasteful because each time it has to loop until it reaches the last stored Node.
</p>

<h2>The Best Approach</h2>
<p>
It turns out that we can reverse the list in a single walk of the linked list.  Look at the following code:
</p>
    :::java
    /**
     * Reverses a singly-linked list of Nodes
     * @param root The root node of the linked list
     * @return The new root node
     */
    public Node reverseList(Node root) {
      Node newRoot = null;
      while(root != null) {
        Node next = root.getNext();
        root.setNext(newRoot);
        newRoot = root;
        root = next;
      }
      return newRoot;
    }

<p>
First, the newRoot variable is created which will be what we return.  For the iteration, we create a temporary node to help do the reversal.  After we swap the next pointers for the Nodes, we set our variables to the next Nodes to be processed to allow us to continue iterating correctly.  By the end, the newRoot variable will be the front of the new list.
</p>
<p>
The key benefits of this algorithm are that it runs in O(n) time and does not use any significant amount of memory because it is modifying the linked list directly.
</p>
layout: default_post
title: How to Reverse a String
category: Technical
date: 2013-03-10 4:4:4
description: Learn how to reverse a String in multiple ways.

<h2>The Question</h2>
<p>
This question is usually given at the beginning of an interview to help the interviewee settle in and get relaxed.  It isn't meant to be tricky at all.  For this, the function must take in a String object and then return the reversed representation.  For example, if the function was passed in "hello" then it will return "olleh".
</p>

<h2>A Naive Approach</h2>
    :::java
    /**
     * Reverses a string.
     * @param input The String to be reversed
     * @return The reversed String
     */
    public String reverseString(String input) {
      String reverse = "";
      for(int x = input.length()-1; x >= 0; x--) {
        reverse += input.charAt(x);
      }
      return reverse;
    }

<p>
This approach definitely works, but something could be better!
</p>

<h2>The Better Solution</h2>
    :::java
    /**
     * Reverses a string.
     * @param input The String to be reversed
     * @return The reversed String
     */
    public String reverseString(String input) {
      StringBuilder reverse = new StringBuilder();
      for(int x = input.length()-1; x >= 0; x--) {
        reverse.append(input.charAt(x));
      }
      return reverse.toString();
    }

<p>
The one major change is that we used a StringBuilder to create the reversed String.  It is much faster to use this instead of constantly creating a new String object for each character that we append. 
</p>
<p>
Doing a simple benchmark where we reversed 20 million String objects with each variation gave these results: 4.875s for the naive approach and 1.069s for the best approach.  A 456% speedup!  Knowing when to use a StringBuilder can certainly impress an interviewer.
</p> 

<p>There are actually several reverse methods found in Java which make this question even more trivial, but I'll leave finding those to you. :)
<p>
The solution will run in O(n) time because it has to walk the length of the String.
</p>
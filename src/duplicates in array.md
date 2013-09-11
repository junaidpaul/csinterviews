layout: default_post
title: Checking for Duplicates in an Array
category: Technical
date: 2013-03-10 5:5:5
description: Learn how to quickly check for duplicates in an array.

<h2>The Question</h2>
<p>Suppose you have an array of integers.  For some reason, you need to check if that array contains any duplicate values in it.  If a duplicate is found, then the method should return and print that it found a duplicate.  Otherwise, it should say that it did not find any duplicates.</p>

<h2>The Naive Approach</h2>
<p>This problem initially might look very easy to you.  An outer loop could loop through all of the array indexes, and a second nested loop would loop through all remaining spots in the array after the outer loop's index.  If at any point the value at the second loop index equals the value at the outer loop index, then a duplicate is found!  Here's some simple code for that:</p>

	:::java
	/**
	 * Checks an array for duplicates.
	 */
	public void checkForDuplicates() {
	  int[] input = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,3,17};
	  for(int x = 0; x < input.length; x++) {
	    for(int y = x+1; y < input.length; y++) {
	      if(input[x] == input[y]) {
	        System.out.println("Duplicate found!");
	        return;
	      }
	    }
	  }
	  System.out.println("No duplicates found.");
	}

<p>Note that such a method would likely take an integer array as a parameter and return a boolean value.  I took a shortcut for clarity and hard-coded an array into the method.</p>

<p>This approach certainly works fine for detecting duplicates.  The problem here is that it does not scale well.  As a computer scientist, you should always be thinking BIG.  If you can't tell from a quick inspection, this algorithm will run in O(n^2) time due to the nested second loop.  This means that as the input array grows, the algorithm will take exponentially longer to complete.</p>

<h2>The Better Solution</h2>
<p>Take a look at this solution and notice the difference.</p>

	:::java
	/**
	 * Checks an array for duplicates.
	 */
	public void checkForDuplicates() {
	  int[] input = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,3,17};
	  HashMap<Integer, Boolean> numbersSeen = new HashMap<Integer, Boolean>();
	  for(int x = 0; x < input.length; x++) {
	    if(numbersSeen.containsKey(Integer.valueOf(input[x]))) {
	      System.out.println("Duplicate found!");
	      return;
	    }
	    else {
	      numbersSeen.put(Integer.valueOf(input[x]), Boolean.TRUE);
	    }
	  }
	  System.out.println("No duplicates found.");
	}

<p>In this solution, we replaced the nested second for loop with a HashMap.  If you remember your data structures, a HashMap has roughly O(1) performance for retrieving and storing key/value pairs.  This code loops through the array and at each iteration checks if the value at the current index is in the HashMap.  If it already exists in the HashMap, then that means a duplicate was found.  This algorithm only takes O(n) time compared to O(n^2) time with the naive approach because the main loop is O(n) and nothing inside the main loop is greater than O(1).</p>

<p>One thing I'd like to point out is that this approach will use more memory to store all of the objects associated with the HashMap.  In general, this is a trade-off that you as a programmer should try to make.  Reducing an algorithm down by orders of magnitude can have a tremendous effect on how long it takes to run.  For large data sets that can translate into hours and days.  Memory is a lot cheaper to come by than extra processors should you ever find yourself working on a program that large!</p>
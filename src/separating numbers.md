layout: default_post
title: Separating Negatives, Positives, and Zeroes
category: Technical
date: 2013-05-05 4:4:5
description: Learn how to separate the positives, negatives, and zeroes in a list of numbers in just one pass.

<h2>The question</h2>
<p>Given an array of integers, return an array that is formatted as such: <code>Negatives / Zeroes / Positives</code></p>
<p>The numbers in each section do not need to be sorted.</p>

<h2>A naive approach</h2>
<p>A slow approach would be to loop through the input array three times, once for each category.  The negatives would be added to the output array first, then the zeroes, and finally the positives.</p>

    :::java
    int input[] = {0,1,2,3,0,0,-1,-2,-3,11,0,0,4};
    int output[] = new int[input.length];
    int pointer = 0;

    for(int x = 0; x < input.length; x++) {
      if(input[x] < 0) //negatives
        output[pointer++] = input[x];
    }

    for(int x = 0; x < input.length; x++) {
      if(input[x] == 0) //zeroes
        output[pointer++] = input[x];
    }

    for(int x = 0; x < input.length; x++) {
      if(input[x] > 0) //positives
        output[pointer++] = input[x];
    }

    for(int x : output)
      System.out.println(x);

<p>This would output <code>-1,-2,-3,0,0,0,0,0,1,2,3,11,4</code> which meets the question's specification.</p>

<h2>A better approach</h2>
<p>This problem can instead be solved with just one pass through of the input array.  The key is to create a start and end pointer for the output array:</p>
    :::java
    int input[] = {0,1,2,3,0,0,-1,-2,-3,11,0,0,4};
    int output[] = new int[input.length];
    int start = 0;
    int end = output.length-1;

    for(int x = 0; x < input.length; x++) {
      if(input[x] < 0)
        output[start++] = input[x];
      else if(input[x] > 0)
        output[end--] = input[x];
    }

    for(int x : output)
      System.out.println(x);

<p>With this approach, we have a start and end pointer which refer to the respective endpoints of the output array.  While looping through the array, we check if the value is positive or negative.  If negative, then we know it belongs in the front so we place it at the current start pointer position and then increment the start pointer.  We do the same thing for positive numbers and the end pointer, but instead decrement the end pointer.</p>

<p>Because integer arrays are initialized by default to 0, we do not need to check for entries being equal to 0.  They are accounted for by whatever leftover spaces there are.</p>

<h2>Inspection</h2>
<p>The first algorithm will run in $O(3n)$ time while the second runs in $O(n)$ time, simply due to the number of loops each method has.  Both solutions have the same asymptotic runtime because they only differ by a constant factor, however, the second solution is still a better implementation.</p>

<p>This question seems simple, but allows the interviewer valuable insight to your thinking.  It's easy to arrive at the first solution and call it a day.  A top candidate will recognize the quicker solution.</p>
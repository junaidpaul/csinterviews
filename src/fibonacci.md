title: The Fibonacci Sequence
category: Technical
date: 2013-09-18 5:5:5
description: Learn about the Fibonacci sequence and questions you may be asked about it.
status: draft

<h2>What is it?</h2>
<p>You have probably heard about the Fibonacci sequence in an early math class.  It is an integer sequence where $0$ and $1$ are the first two numbers, and subsequent numbers are the sum of the previous two.  For example: </p>

$$0,1,1,2,3,5,8,13,21,34,55,89,144$$

<p>This is a great topic for an interview question because of the many ways to implement it.  Now let's get to it.</p>

<h2>Basic solution</h2>
<p>Here is a simple iterative solution:</p>
	:::java
	public int fib2(int n) {
	    int first = 0, second = 1;
	    for(int i=0; i<n; i++) {
	        int temp = first;
	        first = second;
	        second = temp + second;
	    }
	    return first;
	}

<p>This solution will run in $O(n)$ time because it is simply iterating from $0$ to $n$.</p>

<h2>Recursive solution</h2>
<p></p>

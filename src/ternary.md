layout: default_post
title: The Ternary Operator
category: Technical
description: Learn what the Ternary Operator is and how to use it.
date: 2013-03-18 3:3:3

<h2>Writing Cleaner Code</h2>
<p>As a programmer, you should strive to write the cleanest code possible.  Any number of people may need to read through your code at some point, and spending just a little time to make things a bit neater can be extremely valuable.  One trick I like to use is referred to as the <code>Ternary Operator</code>.</p>

<h2>What Is It?</h2>
<p>In this I will explain a typical C-style Ternary Operator.  While programming, how often do you find yourself doing this:</p>
	:::java
	String result;
	if(someCondition == true)
	  result = "It was true!";
	else
	  result = "It was false!";

<p>Writing this over and over can become very tedious.  Luckily, this can be improved to this:</p>
	:::java
	String result = (someCondition) ? "It was true!" : "It was false!";

<p>As you can see, this will increase readability for your code.  One line was able to represent five lines of old code.  Generally if you are using an <code>if/else</code> statement to assign a value to a variable, then you can replace it with the ternary operator.</p>

<h2>Return Values</h2>
<p>The previous example is a great spot for using the Ternary Operator.  Another great use of it is for returning values from methods like this:</p>
	:::java
	//Returns an empty list if key not found
	public List<Books> getList(String author) {
		return (mListMap.get(author) == null) ? new ArrayList<Books>() : mListMap.get(author);
	}

<p>Small things like this can go a long way for increasing readability!</p>

<h2>How To Remember?</h2>
<p>At first, I would always forget the ordering for the Ternary Operator and have to search online for a reference.  Since then, I've come up with this easy way of remembering.  The <code>?</code> always comes first because you are asking the statement a question of whether the statement is true or not.  If it is true, then whatever follows will be executed.  Remember, you have to ask the question first which is why the <code>?</code> comes first.  Otherwise, the code after the <code>:</code> will be executed.  </p>
title: All About Threads
category: Technical
description: Learn what threads are and some common questions you may be asked about them.
date: 2013-09-11 3:3:3

<h2>What Are They?</h2>
<p>Threads allow your program to "multitask".  Imagine you are designing a program that has a GUI (Graphical User Interface) and also accepts user input.  The user clicks a button which then tells your program to perform a long running task.  In a single-thread programming model, the user would have to wait until this long running task is finished before they could press another button.  Luckily, making our program multi-threaded can solve this issue.  More generally, threads help to hide the latency involved with such things as long computation, user input, network or disk access, and more.</p>

<p>When your program has multiple threads the CPU will periodically switch between them, giving your program the illusion of running things concurrently.  In reality, only one instruction can be performed by a CPU core at a time.  With multicore processors, different threads can be running on each core concurrently.</p>

<p><strong>A thread is different from a process.</strong>  A thread is a basic unit for execution that is scheduled by the operating system and executed by the CPU.  A process can be considered a container that can hold multiple threads.  I will explore this further.  With this in mind we can go back to our original GUI example.  To solve the problem of having the UI hang during a long operation we can create a UI thread to separate the logic and keep it responsive.</p>

<h2>Java Example</h2>
<p>Java has two ways of creating and running a thread.  You have the option of subclassing the <code>Thread</code> class to override the <code>start()</code> method.  The other option is to implement the <code>Runnable</code> interface and use that to create the class.</p>

	:::java
	//subclassing method
	new Thread() {
		@Override
		public void run() {
			//the code you want to run in parallel
		}
	}.start();

	//runnable method
	new Thread(new Runnable() {
		@Override
		public void run() {
			//the code you want to run in parallel
		}
	}).start();

<p>The <code>Thread</code> class already implements <code>Runnable</code> itself which is why you can subclass it like so.  I prefer to use the <code>Runnable</code> method over subclassing because you can use those <code>Runnable</code> objects in other parts of your code.  I also prefer to use interfaces over inheritance.</p>

<h2>Quick Terminology</h2>
<p>Threads are a confusing subject because you can no longer think in a purely linear fashion.  For that reason it is best to have a formal study of them.  Nevertheless, I will try to give a brief description of some other aspects to them.</p>

<h4><strong><u>Sleep</u></strong></h4>
<p>A thread can go to sleep by calling the <code>sleep()</code> method which allows the programmer to specify a time in milliseconds or nanoseconds.  This is essentially telling the operating system that it does not need time on the CPU for a specified amount of time.  Note that this is not a precise measurement due to the nature of how the operating system schedules threads.</p>  

<p>When you try to sleep a thread, you may notice that it throws an <code>InterruptedException</code>.  Threads can tell other threads to stop what they are doing, commonly referred to as an interrupt, which will then generate this exception.  From a computer perspective, sleeping for even milliseconds is an enormous amount of time where millions of CPU cycles may already have been executed.  That is why we needed a convenient method of telling threads that are performing long operations to stop.</p>

<h4><strong><u>Interrupt</u></strong></h4>
<p>As you now know, an interrupt is an indication to a thread that it should stop what it is doing and do something else.  Often times, you can just have a thread terminate itself in the event of an interrupt like so:</p>

	:::java
	while(true) {
		try {
			Thread.sleep(4000);
		}
		catch(InterruptedException e) {
			return;
		}
		System.out.println("Hello world.");
	}

<p>If a thread executes for a long time without executing a method that throws an <code>InterruptedException</code> then it should periodically check if it has been interrupted like so:</p>

	:::java
	while(true) {
		System.out.println("Hello world.");
		if(Thread.interrupted())
			return;
	}

<p>Note that <code>interrupted()</code> is static and refers to the current thread while <code>isInterrupted()</code> refers to a thread object.</p>

<h4><strong><u>Joins</u></strong></h4>
<p>This tells one thread to wait until another thread is completed.  Not surprisingly, this is done via the <code>join()</code> method.

<h4><strong><u>Misc</u></strong></h4>
<p>It is useful for debugging to use the <code>getName()</code> method of a thread.</p>

<h2>Under the hood</h2>
<p>As you may realize now, only one thread can hold the CPU at a time.  The operating system schedules threads to have a certain amount of time on the CPU before switching them out for another thread.  There are many algorithms to do this such as First In First Out, Round Robin, and Multi-Level Feedback Queues.  The process of switching between threads, called a context switch, has an inherent overhead cost and means that you can run into scenarios where your program is over-concurrent.  The overhead cost of switching between threads loses more time than you save from concurrency, leading to decreased performance.</p>

<p><strong>Threads are not run in a particular order.</strong>  Which thread gets the CPU next is completely up to the operating system to decide.  It will try to make things fair using its scheduling algorithm, but you cannot assume in your program that there is a defined order of execution.  This is one of the reasons why concurrent programs are hard to design.</p>

<p>As said before, a thread is not equivalent to a process.  A process is heavyweight with larger startup costs comparitively.  The big thing to note is that processes have a separate address space from each other whereas threads all share the address space of the process they belong to.  This means that threads intrinsicly can share memory and variables between each other if they belong to the same process.  If a process wants to communicate or share something with another process then it will need to invoke some sort of inter-process communication.</p>

<p>When the operating system decides that a thread has had enough time on the CPU it will begin a context switch.  What this comes down to is saving the state of the current thread so that it can safely resume where it left off the next time it holds the CPU.  Generally this involves saving information such as the program counter value, register values, and other operating system specific data that is needed.</p>

<p><strong>The operating system can invoke a context switch at any time.</strong>  I will write more about this in later articles about basic synchronization, but in brief the operating system can decide to swap threads on you at any time.  This behavior can lead to some very hard to find race conditions and deadlocks.</p>

<h2>Example</h2>
<p>For now you should check out the comprehensive example from Oracle: <a href="http://docs.oracle.com/javase/tutorial/essential/concurrency/simple.html">Link</a></p>

<h2>Wrap-up</h2>
<p>Parallel computing in traditional programming is not actually occuring in parallel; a single thread can hold the CPU at a given time.  With threads, we can hide the latency of actions such as performing long computation, waiting for user input, network or disk access, and more.  When we create threads, the operating system will schedule how to execute our program's threads for us, creating a context switch each time a thread is swapped off the CPU.</p>
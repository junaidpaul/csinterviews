title: Callbacks Explained
category: Technical
date: 2013-09-07 7:7:7
description: Learn about event-driven code and what a callback is.

<h2>What Is A Callback?</h2>
<p>Callbacks are very common in event-driven code, or executing code based on some sort of event.  This includes user interaction with a GUI, network requests, and even parsers.</p>

<p>A callback is a piece of executable code that is sent as an argument to other code, which is expected to call back (execute) the argument at some convenient time.  OK, you could have just looked that up on Wikipedia.  So what does it really mean?</p>

<p>Each language handles it differently.  In some languages you can pass a function pointer as an argument.  In Java, you typically use an interface.</p>

<h2>Example</h2>

	:::java
	public interface OnClickListener {
		public void onClick(View v);
	}

	View v = findViewById(R.id.someView);
	v.setOnClickListener(new OnClickListener() {
		@Override
		public void onClick(View v) {
			Log.d("click", "the view was clicked!");
		}
	});

<p>This example shows how button presses are typically handled in Android, and should be straightforward enough to follow.  If you are confused about the notation I used here then you should read my article about anonymous classes.  Here we have the interface <code>OnClickListener</code> with its one method.  The method <code>setOnClickListener()</code> accepts this interface.  Internally, the View class handles button clicks like this:</p>

	:::java
	//... inside the View.java class ...
	private OnClickListener mOnClickListener = null;

	public void setOnClickListener(OnClickListener listener) {
		mOnClickListener = listener;
	}

	public void thisViewWasClicked() {
		if(mOnClickListener != null)
			mOnClickListener.onClick(this); //execute callback
	}

<p>If a programmer has called <code>setOnClickListener()</code> then the listener will not be null and the <code>onClick()</code> method will be called.  Separate logic from this will detect the user clicking the screen (an event) to finally trigger the <code>thisViewWasClicked()</code> method.</p>

<h2>Wrap-up</h2>
<p>So here I showed you a very common example of event-driven code.  When an object is clicked, it checks to see if a listener exists.  If it exists then the callback code is executed.</p>
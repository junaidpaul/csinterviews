layout: default_post
title: Why Random is Not So Random
category: Technical
description: Learn about the Random class in Java, it may not be exactly what you think it is!
date: 2013-03-17 3:3:3

<p>I came across this StackOverflow post the other day and thought it was really interesting: <a href="http://stackoverflow.com/questions/15182496/why-does-this-code-print-hello-world">Link</a></p>

<p>Here is the code in question: </p>
    :::java
    public static String randomString(int i) {
        Random ran = new Random(i);
        StringBuilder sb = new StringBuilder();
        for (int n = 0; ; n++) {
            int k = ran.nextInt(27);
            if (k == 0)
                break;
            sb.append((char)('`' + k));
        }
        return sb.toString();
    }

<p>While called like this:</p>
    :::java
    System.out.println(randomString(-229985452) + " " + randomString(-147909649));

<p>So what would you expect this code to output?  You might be surprised to see <code>hello world</code> pop up onto the console!</p>

<h2>Random isn't so random</h2>
<p>What's really happening is that the <code>Random</code> class isn't so random after all.  In fact, the Javadocs for the class clearly states that: </p>

<p><code>An instance of this class is used to generate a stream of pseudorandom numbers.</code></p>

<p>So what does that mean exactly?  Well, in the world of computing it's actually very hard to produce something that is considered a true random number.  Instead, a pseudorandom number generator can be used for most purposes.  This is a function that can produce a set of numbers that exhibits statistical randomness, but is not actually random.  If you use this function then you will get a nice distribution of numbers to use that appear to be random.  For example, if you called a pseudorandom number generator 100 times to generate a number between 1 and 100 then the results would be a fairly even mix of numbers in that range.  This is sufficient for most cases where a random number is needed.</p>

<h2>What is a seed?</h2>
<p>Now we know that the Java <code>Random</code> class is actually a pseudorandom number generator that can produce an almost random number.  If you haven't guessed it by now, it merely is using an advanced algorithm to generate the random number.  A key point here is that because an algorithm is doing the work, it is repeatable!  If two <code>Random</code> objects are freshly created, they will produce the exact same output.  This is where a seed comes in handy.  A seed is considered to be a starting point for the algorithm.  This is how two Random objects can become unique from each other.  Programmers often use the current time as a seed for a pseudorandom number generator such as <code>System.nanoTime()</code>.  And just like freshly created <code>Random</code> objects, two <code>Random</code> objects given the same seed will produce the exact same output.</p>

<h2>Why should I care?</h2>
<p>If you didn't know that a pseudorandom number generator produces repeatable output, then you might have some very big vulnerabilities in your program.  Suppose you were creating a lottery program that would randomly select the next winning number.  If somebody maliciously gains knowledge of the seed that was used (or lack thereof) then they can eventually predict the next winning number!  A pseudorandom number generator should never be used for something as critical as that.</p>

<h2>Truly Random Numbers</h2>
<p>Don't worry, it is possible to get a truly random number with computers.  Most methods involve sampling noise from an environment such as the atmosphere.  The noise cannot be predicted, so even though an algorithm is used to convert the noise to a digital representation a malicious user would not be able to do much.  <a href="random.org">Random.org</a> is an online source to retrieve truly random numbers and a great place to learn more about them.</p>

<h2>Back to the code</h2>
<p>By inspecting the code again you should start to realize what is going on.  Seeding the <code>Random</code> object with <code>-229985452</code> just so happens to have it output the character values for <code>"hello"</code> and then seeding it again with <code>-147909649</code> happens to make it output <code>"world"</code>.  Mystery solved!</p>
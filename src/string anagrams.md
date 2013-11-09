layout: default_post
title: How to Check if Two Strings Are Anagrams
category: Technical
date: 2013-03-10 7:7:7
description: Learn how to tell if two Strings are anagrams of each other.

<h2>The Question</h2>
<p>Given an input of two strings, determine if they are anagrams of each other.</p>

<p>There are several methods of checking if two strings are anagrams of each other.  As a quick reminder, a word is an anagram of another if it means that you could rearrange the characters in one to create the other.  In other words, they have the same amount of each character in the alphabet.</p>

<h2>Approach 1</h2>
<p>A first approach to this involves sorting the two strings by their characters.  Then, a simple equality check can be done to see if the sorted strings match.</p>

    :::java
    public boolean areAnagrams(String first, String second) {
      if(first.length() != second.length()) return false;

      char[] firstChars = first.toCharArray();
      char[] secondChars = second.toCharArray();
      Arrays.sort(firstChars);
      Arrays.sort(secondChars);
      String sortedFirst = new String(firstChars);
      String sortedSecond = new String(secondChars);
      return sortedFirst.equals(sortedSecond) ? true : false;
    }

<p>This algorithm starts by doing a quick check to see if the length of the two strings are equal.  This is a nice quick-fail to avoid wasting time sorting when it doesn't need to be done.</p>
<p>Next, the strings are turned into character arrays.  In this form, we can take advantage of the <code>Arrays.sort()</code> method which performs a <code>Dual-Pivot Quicksort in </code>$O(n*lg(n))$ <code>time</code>.  Now we have our sorted strings.  A simple <code>.equals()</code> of the two strings can done to finally see if the strings are anagrams of each other.</p>

<h2>Approach 2</h2>
    :::java
    public boolean areAnagrams(String first, String second) {
      if(first.length() != second.length()) return false;

      int alphabet1[] = new int[26];
      int alphabet2[] = new int[26];

      for(int x = 0; x < first.length(); x++) {
        if(Character.isLetter(first.charAt(x)) && Character.isLetter(second.charAt(x))) {
          alphabet1[first.charAt(x) - 'a']++;
          alphabet2[second.charAt(x) - 'a']++;
        }   
        else
          return false;
      }
      
      for(int x = 0; x < 26; x++) {
        if(alphabet1[x] != alphabet2[x])
          return false;
      }
      return true;
    }

<p>First off, this approach makes the assumption that the strings are English words because we create two arrays of size 26 (26 letters in the alphabet).  Similarly to the first approach, we perform a quick check on the size of the strings as a quick-fail.  After that, we walk the strings and increment the index of the characters in the strings.  For example, if we perform a <code>.charAt(0)</code> of the first string and it returns <code>'a'</code>, then we know to increment <code>alphabet1[0]</code> because <code>'a'</code> is the first index of the alphabet. Now we know the frequency of each character in both strings.  Comparing the two alphabet arrays will tell us if the strings are anagrams or not.</p>

<h2>The Difference</h2>
<p>The first approach is more general because it sorts the strings by their lexicographical value.  The second string only works if the strings contain characters between <code>'a'</code> and <code>'z'</code>.  This is obviously not the case for many strings, though some may argue that such a case violates the definition of an anagram if non-alphabetic characters exist.  This could be adjusted by increasing the size of the array to accommodate for more characters, but could get messy very quickly.  </p>
<p>When compared for runtime, the second algorithm is faster than the first because it really only has to walk the string which takes $O(n)$ time.  The first algorithm has to sort with an $O(n*lg(n))$ quicksort.</p>

<h2>Which Algorithm to Choose?</h2>
<p>So which one should you choose in an interview?  Well, both should be acceptable because they each have their own weaknesses.  If you suggest both algorithms to your interviewer, then that typically leads to a predictable follow-up question: which one would you choose?  Little does the interviewer know that you just set a trap and they fell for it.  It's always a good idea to lead your interviewer to asking you an easy question.  A good answer to this would be that it really depends on the application.  Is the runtime of the algorithm absolutely critical?  If so, then the second algorithm will run faster given large inputs.  Or is reliability what matters most?  Because the first algorithm sorts the strings by their lexicographic value, it does not have to take into account the many edge cases of the second algorithm such as not all alphabets having 26 characters.  Remember that the reasoning behind the choice is often more important than saying "Pick algorithm 1/2!!"</p>
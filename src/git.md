layout: default_post
title: Git Basics
category: Technical
date: 2013-10-15 4:4:5
description: Learn the basics of Git and why version control systems are so powerful!
status: draft

<h2>Preface</h2>
<p>I will mostly be paraphrasing the official Getting Started guide of Git found <a href="http://git-scm.com/book/en/Getting-Started-Git-Basics">here</a>.  This beginner guide is very good and hopefully this will act as supplemental information.</p>

<h2>What is version control?</h2>
<p>During your first year of programming, you might find yourself creating your own ad-hoc version control system.  Have you ever finished a project and looked at the files you created only to find names such as <code>Solution.java</code>, <code>Solution1.java</code>, <code>Solution11.java</code>, <code>Solution1Backup.java</code>, and so on?  This is a perfect situation to migrate over to a version control system.  A version control system will handle keeping track of all these different revisions for you.</p>

<p>For this tutorial we will be covering Git, an extremely popular distributed version control system.  A key thing to note here is that it is distributed, meaning that every developer will have their own copy of the code to work with.</p>

<h2>Typical Workflow</h2>
<p>Let me start by first describing a typical workflow one might use with Git.  First, the project that you want to work on is cloned.  You work on editing and creating files for the project, and then add them to the staging area.  Then you commit the files in the staging area to the Git repository.  After, you keep editing and creating files to the project while continuing to add them to the staging area before committing.  Then, a fellow developer commits their code to the repository.  You pull their changes, merge the code, and continue working.</p>

<h2>The Three States</h2>
<p>The previous example is overwhelming, I understand that, so I'll begin by explaining the different parts to Git.</p>

<p>The <strong>Git directory</strong> is where the metadata and object database for your project is stored.  Typically this is found in the <code>.git</code> folder of your project and you can browse through it to get a feel of how Git tracks things internally.</p>

<p>The <strong>staging area</strong> is where you add files that you want to eventually commit to the Git directory.  This helps you organize exactly what you want to commit so that you can better track your files.  Keeping only relevant files in each commit will make it much easier on yourself if you need to revert a change in the future.  Adding a file to the staging area essentially creates a snapshot of it.</p>

<p>The <strong>working directory</strong> is your "checkout" of the code.  I mentioned earlier that Git is distributed so that each developer has a full working copy of the code.  When you clone a project it creates your working directory.  The files that you modify will be from the working directory.</p>

<h2>Starting out</h2>
<p>Now that you know about the different states of files in a Git repository, it's time to get started.  Here are three commands:</p>

<h4><strong>git add</strong> <i>filename</i></h4>
<p>This will add files to the staging area.</p>

<h4><strong>git rm</strong> <i>filename</i></h4>
<p>This will remove files to the staging area.</p>

<h4><strong>git status</strong></h4>
<p>This will show you the current state of your staging directory including files that are not being tracked.</p>

<p>These three commands will help you manipulate the files in your staging area.  When you first start a project, none of your files will be tracked.  If you create a few projects and then run the <code>git status</code> command you will see what I mean.  When you are ready to make a commit, add the files to your staging area with the add command, and then check the status again.

<h2>Getting ready to commit</h2>
<p>Now you have the files you want to commit in your staging area.  All that's left is to commit them to the Git repository using the following command:</p>

<h4>git commit</h4>
<p>Though it is always best to leave a message with your commit like so:</p>

<h4>git commit -m "Added some new files"

<p>It's good to label your commits with a message so that you can quickly remember what is in each.  Once you have made some commits you can view your history using the <code>git log</code> command.</p>
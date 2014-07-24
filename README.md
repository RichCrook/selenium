selenium
========

java -jar selenium-server-standalone-2.42.jar -port 4444

Test Planning 
Test Planning is one of the keys to project success: 
Gathering Requirements 
Functional Decomposition 
Risk Based Testing Analysis 
Develop Test Plans and Procedures 

Test Planning 
Test Planning is one of the keys to project success: 
Gathering Requirements 
Functional Decomposition 
Risk Based Testing Analysis 
Develop Test Plans and Procedures 
Requirements Gathering 
Project Plan or Business Requirements Spec – We might expect a business plan including the specific business requirements in general or for a specific project.
Software Requirements Specification – A software specification for websites includes supported browsers and mobile devices.
Functional Design Document – A functional design specification is a blueprint that developers sign off on before any coding is done.
Feature Specification Document – This document outlines the new features for the project that are to be implemented.
Use Cases – We could create or derive some use cases based upon users who interact with the clone IMDB website
Wireframes – Wireframes provide a visual guide to was is to be implemented and are critical for front-end development and can assist automation engineers to begin test case design or writing.
Stakeholders – Important pieces of a project, application flows, and other critical aspects of the project are important to identify to mange expectations of those Stakeholders and to provide guidance and prioritization development/QA teams for the tasks they are to work on.
Test Planning – RBT Analysis 
Identify the most critical paths in the application and flows or points at which the application might break. We cannot reasonably test all possible permutations so we need to strategize on optimizing resources.
Test Planning – Test Plans 
IEEE 829 defines many types of test specifications – “If it’s not written down, it didn’t happen.” 

Testability as a requirement for Development: Provide a unique and meaningful name property for all elements under test. This could be done through and schema where any developer creating a page would already know what a name for an element might be. 
Functional testing: 
Run Smoke, Sanity, Critical Path tests 
Check all links and web pages 
Page Download Times and Browser Rendering: 
No one likes a slow website Load testing and performance usually done late in 
the test cycle 
Measure web page download performance early – Part of Sanity/Smoke test script. – Run multiple times and average. 
Page Download Time and HTML elements: 
Measure HTML element download times – HttpWatch (works with both Firefox & IE, has an API) – tools.pingdom.com (to demo object downloads) – Yslow (Firefox addon) 
Cross Browser Testing 
Various combinations of FF, IE and WindowsOS, XP/IE6,XP/IE7 

Login - A user logs in with one of several accounts
Test case one IMDB
Test case two Amazon
Test case three Facebook
Test Case four Google
Registration – A user registers a new account 
Given seven fields with one radio button that has two values and one drop-down that has n number of values the theoretical number of possible test case permutations is around 4,000 test cases for highest accuracy. 
But in practicality will might just have eight tests:
one test for each bad field
one test for the happy path

Watchlist – Add a Movie to the User's Watchlist page logged in and logged out
Movie Page – The desired movie page renders as expected in a logged in and out state
Movie image is present
Movie title is present
Rating is present
Run time is present
Genres are present 
Date movie is present
Rating star is present with a value
Your rating functionality is working
Description is present
Director is present
Homepage – The homepage is rendering as expected for a logged in an d logged out user
Trailers – Clicking on the Trailer page to see that a trailer has launched
Search – Enter in a valid movie and and invalid movie and note pop up list
Share – Test whether a pop up movie has launched

Personal Details
Change Password
Change E-Mail Address
Change ID

Some possible test cases:

Site Preferences
Movie Review settings
Your Boards Profile
My Contacts for helpdesk
View your contributions
Swiki Notification List
Delete your account
IMDb User Profile Page FAQ
View WatchList
Create New WatchList
Verify Home Button works
Verify List works
Verify Header list works
Movie, TV & Showtimes dropdown
Celebs, Events and Photos dropdown
New And Community 
Showtimes and Tickets
Change location on showtimes
Theatres are listed
Addresses
Showtimes
Get Tickets launches a pop up
reviews
list actors
videos
photos
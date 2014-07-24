selenium
========

java -jar selenium-server-standalone-2.42.jar -port 4444

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
Prioritize what should be tested first. 
Not doing so explains why big bugs are found at the end of a test cycle; its human nature to test the easy functionality first. 
Identifying critical aspects of an application and the “path most tred”, points or places where an application might break
Test Planning – Test Plans 
IEEE 829 defines many types of test specifications – “If it’s not written down, it didn’t happen.” 
Practical Suggestions for Test Planning : 
Web Analytics (for existing websites) 
Planning Test Automation? – Testability as a requirement for Development 
Production Monitoring 
Test Planning ‐ Testability 
Planning Test Automation? 
Testability as a requirement for Development: Provide a unique and meaningful name property for: 
– Every actionable html object on the page. (entry‐fields, buttons, radio buttons, dropdown list boxes, images, links, etc.) 
– Every table object that requires testing. 
– Every response that requires testing. The response may be in tables, spans, divs, lis, etc. 
Test Planning ‐ Testability 
Testability as a requirement for Development: 
Populate the ‘id’ and ‘alt’ tags to give QA more alternatives to identify an object during scripting. 
– SEO and 508 Compliance contribute to this recommendation as well. 
Use a naming convention that includes the function or purpose of the given object. 
Do not change any HTML element property name (including id & alt tags) from release to release. 
Test Planning ‐ Monitoring 
Production Monitoring: 
Ensure your site and applications are performing. 
Identify, resolve and prevent issues. 
Develop an escalation policy, triage, remediate, and confirm resolution. 
Use automated daily smoke tests to supplement monitoring from a customer or partner perspective. 
Discuss this during the requirements phase – What, how, where and who? – The wrong time is the day of deployment. 
Configuration Management 
Manage software configurations: 
Audit configuration after push to QA/Prod – Use mySite.com/revision.txt to confirm – Output contains Build Version, Date & Time 
Establish method to directly access web servers – Avoid round‐robin approach behind load balancers. – http://web#‐www.mySite.com/revision.txt 
Functional Testing 
Functional testing: 
Run Smoke, Sanity, Critical Path tests 
Check all links and web pages 
Usability Inspection 
Usability Inspection: 
Navigation Page Content Intuitive 508 Compliance ‐ accessibility Search 
Sitemap Help 
Usability – User Experience 
Page Download Times and Browser Rendering: 
No one likes a slow website Load testing and performance usually done late in 
the test cycle 
Measure web page download performance early – Part of Sanity/Smoke test script. – Run multiple times and average. 
Track page download trends from release to release. – Test script writes download times to csv. 
Usability – Drilling Down 
Page Download Time and HTML elements: 
Measure HTML element download times – HttpWatch (works with both Firefox & IE, has an API) – tools.pingdom.com (to demo object downloads) – Yslow (Firefox addon) 
Cross Browser Testing 
Cross Browser Testing project: Created and used a CBT lab. 
– Various combinations of FF, IE and WindowsOS • XP/IE6,XP/IE7 
• Vista/IE7 • XP/Firefox 
– Ran automated regression tests on each combination. – Discovered many cosmetic defects. – No functional errors found. – Many companies use Selenium. 
Security Testing 
Security – start simply (perhaps you already do?): 
Invalid inputs in text entry fields and forms SSL– https is used where appropriate (e.g. forms) Internal URLs not accessible (unless logged in) Confirm no access to web server directories XSS – Cross Site Scripting 
Managing the defect lifecycle: 
Issues are detailed, descriptive, and concise. 
Ensure severity and priority are appropriate. 
Ensure there are no unassigned issues. 
Hold weekly mandatory review meetings between QA & stakeholders 
Write a defect, write a test case (if none exists) – Copy steps to reproduce into a new test case. ^C^V – Great way to “beef up” regression test suite. 
Test Tools ‐ Security 
Security: OWASP.org – web security testing tools Ethical Hacker Network HP Dev Inspect (for programmers) HP QA Inspect (for QA testing) HP Web Inspect (for Production) 
Hosted services; McAfee for production security testing. 
Quality Nuggets 
Before Deployment Day! Run your regression test scripts in Prod – why? 
–  Deployment failed, troubleshooting focused on new release, root cause was a pre‐existing condition in Prod. 
–  Discovering issues before deployment eliminates the confusion and unnecessary troubleshooting from assuming that a new deployment caused the problem. 
–  By running automated regression the evening before a deployment, several issues have been found since, some serious. 
User is aware of the basics of test automation
User has planned the test automation activity, by considering the scope, objectives, requirements, schedule and budget
User has gone through the process of "Test Automation Tool Build or Buy" and has taken a decision of buying a tool or getting a open-source tool

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
Director is 
Homepage – The homepage is rendering as expected for a logged in an d logged out user
Trailers – Clicking on the Trailer page to see that a trailer has launched
Search – Enter in a valid movie and and invalid movie and note pop up list
Share – Test whether a pop up movie has launched
Personal Details
Change Password
Change E-Mail Address
Change ID
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
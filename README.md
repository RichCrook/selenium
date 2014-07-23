selenium
========
It was great talking with you.  The "DEVELOPER TASK" is a coding test that is sent to potential python developers.   Please complete the QA TASK and respond with your results.
 
QA TASK
State any assumptions and/or additional details needed for proper testing
Define test cases that can be used in test automation
Code some examples of these test cases
Not all defined test cases need to be coded
The attached "img_count_output.txt" file is a piped result of executing the DEVELOPER TASK.
Use your desired language
Must be able to run in standard Linux terminal
Note any requirements needed to run the the tests

DEVELOPER  TASK

We want to create an IMDB clone, with the twist that we only display
the pages for movies that are in theaters. As part of this, we want to
get a count of images to approximate how much storage space we need.
 
You need to do the following:
- Use the rottentomatoes.com API to get the list of movies currently in theaters
 
- For-each movie in the list, download it's matching IMDB page and get
  a count of the number of images in the page.
 
Write a Python program, img_count.py, that implements this.
 
OUTPUT
A JSON list of objects that looks like this:
[
 {
    "url": "http://www.imdb.com/title/tt1229340", 
    "count": 71, 
    "imdb_id": "1229340"
  }
]
Each movie in the in-theaters list must have an entry in the result.
 
REQUIREMENTS
The program must be a Python file named img_count.py
 
It must be able to run in a standard Linux terminal
 
img_count.py must be able to be run as either a shell script or via %
python img_count.py
 
img_count.py must print the expected output (as above) to stdout
 
The program must complete execution in under 8 seconds, and will be
timed using the Linux 'time' command.​


IMAGE ASSUMPTIONS
image/gif
image/png
image/jpeg

We can use the output of the script to drive the ui test
verify that the api for the rottentomates matches the output of the test
assume standard form ui javascript error messaging
validate json
guest settings versus logged in


Each test case should include an id title
objective
expected results
steps


– Content Management System changes 
What are some possible use cases?
Someone uses an ipad
someone uses a phone
spot testing things manually with real devices
design happy paths first




positive tests

If we are creating a clone then we assume it should have the same functionality
Login
Register
Search
watchlist
trailer
share

use test test to count the images in selenium

full tests

http://ios-driver.github.io/ios-driver/?page=setup


java -jar ios-server-standalone-0.6.6-SNAPSHOT.jar -aut path/to/aut.app -port 4444

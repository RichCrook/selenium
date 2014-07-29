#rottentom.py

#http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=[your_api_key]
import json
import urllib2

# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=ag7zkn8gc6bmcdsfhnb3vpfj"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(url))

#print type(data) is dict
# print the result
#for key, value in data.iteritems():
	#print key, value
    #print key, 'corresponds to', data[key]
#print data['movies'][0]['alternate_ids']['imdb']
for item in data['movies']:
  mylist = item.values()
  print mylist
  #for c in range(len(c)):
   #print c
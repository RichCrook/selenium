import json
file = open('img_count_output.txt', 'r')

d = json.loads(file.read())
print d[0]["url"]
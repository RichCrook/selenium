import json
  
json_data = open('img_count_output.txt')
data = json.load(json_data)
for item, value in data:
   if item == 'url':
     print value
import json 
import requests





result = requests.get("https://app.mobalytics.gg/lol/champions/akshan/counters")

# json_string = json.dumps(result.json)
print(result.json)
with open('normal.html', 'wb') as outfile:
    outfile.write(result.content)
# print(result.content) 
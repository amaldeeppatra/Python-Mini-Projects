import requests
import json

res = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
data = res.text
parse = json.loads(data)
fact = parse['text']
print(fact)
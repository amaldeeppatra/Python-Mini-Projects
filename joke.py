import requests
import json

res = requests.get("https://v2.jokeapi.dev/joke/Dark?type=twopart")
data = res.text
parse_json = json.loads(data)
setup = parse_json['setup']
delivery = parse_json['delivery']
# print(parse_json)
print(setup)
print(delivery)
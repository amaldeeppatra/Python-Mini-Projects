import requests

res = requests.get("https://techy-api.vercel.app/api/text")
print(res.text)
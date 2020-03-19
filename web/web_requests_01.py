import requests

url = "https://www.fortytwo.sg/furniture/dining-kitchen"
req = requests.get(url)
print(req.text)



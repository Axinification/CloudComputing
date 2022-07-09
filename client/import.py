import requests

endpoint = "http://20.238.8.233/import/"
response = requests.post(endpoint, json={"author": "chmielewska"})

print(response.json())
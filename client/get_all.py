import requests

endpoint = "http://20.238.8.233/books/"
response = requests.get(endpoint)

print(response.json())
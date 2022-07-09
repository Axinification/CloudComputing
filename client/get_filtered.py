import requests

endpoint = "http://20.238.8.233/books?from=2000&to=2001"
response = requests.get(endpoint)

print(response.json())
import requests

endpoint = "http://20.238.8.233/books/1"
response = requests.delete(endpoint)

print(response)
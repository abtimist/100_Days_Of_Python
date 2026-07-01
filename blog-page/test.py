import requests

response=requests.get(url="https://api.npoint.io/dbc3a0f6d0a12c72b99a")
posts = response.json()[1]['subtitle']

print(posts)
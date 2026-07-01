import requests

response = requests.get("https://api.agify.io", params={"name": "michael"})
age =  response.json()["age"]
print(age)
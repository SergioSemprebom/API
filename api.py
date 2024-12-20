import requests

URL = 'https://pokeapi.co/api/v2/pokemon/15'
response = requests.get(URL, verify=False)
data = response.json()
print(data)
import requests

# executando o response em aplicao externa
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/15', verify=False)

# trazendo a resposta
data = response.json()

# com todos os tipos de pokemon
data_types = data['types'] #Supondo que 'data é o dicionario com dados

# criando uma lista vazia
types_list = []

# adicionando todos os tipos de pokemon nessa lista
for type_info in data_types:
    types_list.append(type_info['type']['name'])

# transformando essa lista numa string
types = ', '.join(types_list)
print(data['name'], types)

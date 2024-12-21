import requests
from pydantic import BaseModel

# descelerializar = transforma um ARQ.json em um objeto python

class PokemonSchema(BaseModel): # Contrato de dados, schema de dados, a view dos dados

    name: str
    type: str
    
    class Config:
        orm_mode = True

def pegar_pokemon(id: int) -> PokemonSchema:
    # executando o response em aplicao externa
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()# trazendo a resposta
    data_types = data['types'] #Supondo que 'data é o dicionario com dados com todos os tipos de pokemon
    types_list = [] # criando uma lista vazia
    for type_info in data_types:# adicionando todos os tipos de pokemon nessa lista
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list) # transformando essa lista numa string

    return PokemonSchema(name=data['name'], type=types)

if __name__ =='__main__':
    print(pegar_pokemon(10))
    print(pegar_pokemon(25))
    print(pegar_pokemon(17))
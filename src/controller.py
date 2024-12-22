# Faz o controle de todos as funcoes
import requests
from db import SessionLocal, engine, Base 
from models import Pokemon
from schema import PokemonSchema
import json

Base.metadata.create_all(bind=engine)

def fetch_pokemon_data(pokemon_id: int):
    # executando o response em aplicao externa
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    if response.status_code == 200:
        data = response.json()# trazendo a resposta
        with open(f'{data['name']}.json', "w") as f:
            json.dump(data, f)
        types = ', '.join(type_info['type']['name'] for type_info in data['types'])

        return PokemonSchema(name=data['name'], type=types)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon


    
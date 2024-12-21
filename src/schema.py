from pydantic import BaseModel

# schema do PYDANTIC 

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True
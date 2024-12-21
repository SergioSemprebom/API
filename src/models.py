# Representação do banco de dados
from sqlalchemy import Column, Interger, String, DateTime
from sqlalchemy.sql import func
from db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Interger, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now()) # CAmpo adicionado
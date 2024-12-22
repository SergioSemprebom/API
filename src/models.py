# Representação do banco de dados
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now()) # Campo adicionado
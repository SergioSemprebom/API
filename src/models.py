# Representação do banco de dados
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from db import Base

Base = declarative_base()




class Pokemon(Base):
    __tablename__ = 'pokemons'  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())  # Data/hora com timestamp automático

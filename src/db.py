from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACHEMY_DATABASE_URL = "sqlite:///./pokemon.db"
engine = create_engine(SQLACHEMY_DATABASE_URL)
SessionLocal = sessionmaker()
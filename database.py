from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:div8login@localhost:5432/divya"
engine = create_engine(db_url)
session = sessionmaker(autocommit= False, autoflush = True, bind=engine)
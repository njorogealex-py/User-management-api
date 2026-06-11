from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  #Allows us to get the URL from the.env file

engine = create_engine(DATABASE_URL)  #The actual connection to PosgreSQL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  #when called it gives us a fresh db. session

Base = declarative_base()  #Base is the foundation class that all database models inherit from.

def get_db():
    db = SessionLocal() 
    try:
        yield db    #Means hand over the session to the function that needs it currently.
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:manage@localhost:5432/hospital"

engine = create_engine (SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

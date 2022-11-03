from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

# load .env
load_dotenv()

id = os.environ.get("MARIADB_ID")
pw = os.environ.get("MARIADB_PASSWORD")
host = os.environ.get("MARIADB_HOST")

SQLALCHEMY_DATABASE_URL = f"mariadb+pymysql://{id}:{pw}@{host}:3306/network_project"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

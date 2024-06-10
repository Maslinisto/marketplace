from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()
class Base(DeclarativeBase):
    pass

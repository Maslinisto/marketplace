from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:bebra@localhost:5432/marketplace")
sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()
class Base(DeclarativeBase):
    pass

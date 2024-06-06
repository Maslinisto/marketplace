import psycopg2
from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
#from app.config import settings
#database_url = settings.DATABASE_URL
#print('2', database_url)
engine = create_engine("postgresql+psycopg2://postgres:bebra@localhost:5432/marketplace")
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Book")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

Base.metadata.create_all(engine)
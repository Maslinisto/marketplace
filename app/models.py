from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import  relationship
from timestamp import TimestampMixin
from database import engine, Base

class Author(TimestampMixin, Base):
    __tablename__ = 'authors'
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship("Book")

class Book(TimestampMixin, Base):
    __tablename__ = 'books'
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))


Base.metadata.create_all(engine)
#new_author = Author(first_name="John", last_name="Doe")
#session.add(new_author)
#session.commit()
#
#
#author = session.query(Author).first()
#author.first_name = "Jane"
#session.commit()
#session.close()
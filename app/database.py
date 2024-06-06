from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String, DateTime, create_engine, event, inspect
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.declarative import declared_attr

engine = create_engine("postgresql+psycopg2://postgres:bebra@localhost:5432/marketplace")
Base = declarative_base()

class Timestamp(Base):
    __tablename__ = 'timestamp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

class TimestampMixin:
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True)

    @staticmethod
    def update_timestamp(mapper, connection, target):
        table_name = target.__tablename__
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()
        timestamp_record = session.query(Timestamp).filter_by(table_name=table_name).first()
        if not timestamp_record:
            timestamp_record = Timestamp(
                table_name=table_name,
                created_at=datetime.utcnow()
            )
            session.add(timestamp_record)
        timestamp_record.updated_at = datetime.utcnow()
        session.commit()
        session.close()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, 'before_insert', cls.update_timestamp)
        event.listen(cls, 'before_update', cls.update_timestamp)

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

# автоматическое обновление времени в таблицах
session = sessionmaker(bind=engine)()
inspector = inspect(engine)
existing_table_names = inspector.get_table_names()

for table_name in existing_table_names:
    if not session.query(Timestamp).filter_by(table_name=table_name).first():
        timestamp_record = Timestamp(
            table_name=table_name,
            created_at=datetime.utcnow()
        )
        session.add(timestamp_record)
session.commit()


new_author = Author(first_name="John", last_name="Doe")
session.add(new_author)
session.commit()


author = session.query(Author).first()
author.first_name = "Jane"
session.commit()
session.close()
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker
from app.database import Author

engine = create_engine("postgresql+psycopg2://postgres:bebra@localhost:5432/marketplace")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

s1 = Author(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko',
)

s2 = Author(
    first_name = 'Valeriy',
    last_name = 'Golyshkin',
)

print('brbara', session.query(Author).all())

query = select(Author)
result = session.execute(query).mappings().all()
print(result)

session.close() #нужен ли close после коммита?
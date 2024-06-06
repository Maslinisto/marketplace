from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session, sessionmaker
from app.database import Author

engine = create_engine("postgresql+psycopg2://postgres:bebra@localhost:5432/marketplace")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

#s1 = Author(
#    first_name = 'Dmisatriy',
#    last_name = 'Yatsdaenko',
#)
#
#s2 = Author(
#    first_name = 'Valddderiy',
#    last_name = 'Golyashkin',
#)

#print('brbara', session.query(Author).all())

query = select(Author)
result = session.execute(query).mappings().all()
#print(result)

query = update(Author).where(Author.id==1).values(last_name="daaaas")
result = session.execute(query)
session.commit()
session.close() #нужен ли close после коммита?

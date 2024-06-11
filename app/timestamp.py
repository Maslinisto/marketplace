from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, event
from sqlalchemy.orm import sessionmaker
from app.database import Base, engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Timestamp(Base):
    __tablename__ = 'timestamp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

class TimestampMixin:
    @staticmethod
    def update_timestamp(mapper, connection, target):
        table_name = target.__tablename__
        session = SessionLocal()
        try:
            timestamp_record = session.query(Timestamp).filter_by(table_name=table_name).first()
            if not timestamp_record:
                timestamp_record = Timestamp(
                    table_name=table_name,
                    created_at=datetime.utcnow()
                )
                session.add(timestamp_record)
            timestamp_record.updated_at = datetime.utcnow()
            session.commit()
        finally:
            session.close()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, 'before_insert', cls.update_timestamp)
        event.listen(cls, 'before_update', cls.update_timestamp)

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Register the event listener for table creation
        event.listen(cls.__table__, 'after_create', initialize_timestamp_record)

# Дата создания
def initialize_timestamp_record(target, connection, **kw):
    table_name = target.name
    session = SessionLocal()
    try:
        if not session.query(Timestamp).filter_by(table_name=table_name).first():
            timestamp_record = Timestamp(
                table_name=table_name,
                created_at=datetime.utcnow()
            )
            session.add(timestamp_record)
        session.commit()
    finally:
        session.close()

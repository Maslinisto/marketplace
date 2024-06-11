from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, event
from sqlalchemy.orm import sessionmaker
from app.database import Base, engine

SessionLocal = sessionmaker(bind=engine)

class Timestamp(Base):
    __tablename__ = 'timestamp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
Base.metadata.create_all(bind=engine)
class TimestampMixin:
    @classmethod
    def update_timestamp(cls, mapper, connection, target):
        table_name = target.__tablename__
        session = SessionLocal()
        print(f"Updating timestamp for table: {table_name}")
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
            print(f"Timestamp for table {table_name} updated successfully")
        except Exception as e:
            print(f"Error updating timestamp for table {table_name}: {e}")
        finally:
            session.close()

    @classmethod
    def initialize_timestamp_record(cls, target, connection, **kw):
        table_name = target.name
        session = SessionLocal()
        print(f"Initializing timestamp record for table: {table_name}")
        try:
            if not session.query(Timestamp).filter_by(table_name=table_name).first():
                timestamp_record = Timestamp(
                    table_name=table_name,
                    created_at=datetime.utcnow()
                )
                session.add(timestamp_record)
                session.commit()
                print(f"Timestamp record for table {table_name} initialized successfully")
            else:
                print(f"Timestamp record for table {table_name} already exists")
        except Exception as e:
            print(f"Error initializing timestamp record for table {table_name}: {e}")
        finally:
            session.close()

    @classmethod
    def __declare_last__(cls):
        print(f"Registering event listeners for {cls.__tablename__}")
        event.listen(cls, 'before_insert', cls.update_timestamp)
        event.listen(cls, 'before_update', cls.update_timestamp)

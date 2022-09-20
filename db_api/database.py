from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager


SQLALCHEMY_DATABASE_URL = "postgresql://ale:progetto@db/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#db: Session = SessionLocal()
@contextmanager
def get_session():
    db: Session = SessionLocal()

    try:
        yield db
    except:
        db.rollback()
        raise
    else:
        db.commit()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_DATABASE_URL = 'localhost:5433/test'

engine = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread': False})

Session = sessionmaker(autocommit=False, autoflush=False, bin=engine)

Base = declarative_base()


def get_session() -> Session:
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()

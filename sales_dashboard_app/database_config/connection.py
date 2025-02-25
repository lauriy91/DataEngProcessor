from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

# RESOLVER!!!!
# DATA_DIR = Path("sales_dashboard_app/data")
# DB_FILE = DATA_DIR / "sales_dashboard_data.db"
DB_FILE = Path(__file__).resolve().parent / "C:/Users/Laura Rodriguez King/Documents/Development/DataEngTest/sales_dashboard_app/data/sales_dashboard_data.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_engine():
    return engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

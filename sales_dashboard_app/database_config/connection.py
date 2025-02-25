from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./sales_dashboard.db"
# sql_connection = "DRIVER={ODBC Driver 17 for SQL Server};db_host,db_port;db_name;db_user;db_pass"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

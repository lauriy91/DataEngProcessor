from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, Date
from sqlalchemy.orm import sessionmaker, declarative_base
import polars as pl

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///etl_processor/data/sales_data.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Definición de modelos con SQLAlchemy
class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    category = Column(String)
    product = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    total_sales = Column(Float)
    day_of_week = Column(String)
    high_volume = Column(Boolean)

class AggregatedMetric(Base):
    __tablename__ = "aggregated_metrics"
    category = Column(String, primary_key=True)
    avg_price = Column(Float)
    total_revenue = Column(Float)
    top_sales_day = Column(String)

class Outlier(Base):
    __tablename__ = "outliers"
    transaction_id = Column(Integer, primary_key=True)
    category = Column(String)
    product = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    total_sales = Column(Float)
    outlier = Column(Boolean)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Cargar los datos procesados
df_cleaned = pl.read_csv("etl_processor/data/final_data.csv")

# Iniciar sesión con SQLAlchemy
session = SessionLocal()

# Insertar datos en Transactions
for row in df_cleaned.iter_rows(named=True):
    session.add(Transaction(**row))

# Insertar métricas agregadas
df_metrics = pl.read_csv("etl_processor/data/category_metrics.csv")
for row in df_metrics.iter_rows(named=True):
    session.add(AggregatedMetric(**row))

# Insertar outliers
df_outliers = df_cleaned.filter(pl.col("outlier") == True)
for row in df_outliers.iter_rows(named=True):
    session.add(Outlier(**row))

# Confirmar cambios en la base de datos
session.commit()
session.close()

print("Datos almacenados en SQLite correctamente usando SQLAlchemy.")

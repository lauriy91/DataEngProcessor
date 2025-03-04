import polars as pl
from database_config.connection import SessionLocal, engine
from pathlib import Path
from database_config.connection import Base
from database_config.models import Transactions, CategoryMetrics, Outliers

Base.metadata.create_all(engine)

# Roots
DATA_DIR = Path("sales_dashboard_app/data")
INPUT_FILE = DATA_DIR / "transformed_complex_data.csv"
DB_FILE = DATA_DIR / "sales_dashboard_data.db"

df_transformmed = pl.read_csv(INPUT_FILE)

# Sign in session
session = SessionLocal()

# Save transactions db data from the cleaned script file
for row in df_transformmed.iter_rows(named=True):
    session.add(Transactions(**row))

# Save category metrics db data from the transform complex script file
df_metrics = pl.read_csv("etl_processor/data/category_metrics.csv")
for row in df_metrics.iter_rows(named=True):
    session.add(CategoryMetrics(**row))

# Save outliers db data from the transform complex script file
df_outliers = df_transformmed.filter(pl.col("outlier") == True)
for row in df_outliers.iter_rows(named=True):
    session.add(Outliers(**row))

# Close the connection
session.commit()
session.close()

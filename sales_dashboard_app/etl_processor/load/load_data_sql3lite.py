import polars as pl
from pathlib import Path
import sqlite3

# Roots
DATA_DIR = Path("sales_dashboard_app/data")
INPUT_FILE = DATA_DIR / "transformed_complex_data.csv"
DB_FILE = DATA_DIR / "sales_dashboard_data.db"

df = pl.read_csv(INPUT_FILE)

# Connection to the database sqlite 3
conn = sqlite3.connect(DB_FILE)

# Save transactions db data from the cleaned script file
df.to_pandas().to_sql("transactions", conn, if_exists="replace", index=False)

# Save category metrics db data from the transform complex script file
category_metrics = df.select(
    ["category", "average_price", "total_revenue", "day_with_highest_sales"]
).unique()

category_metrics.to_pandas().to_sql(
    "category_metrics", conn, if_exists="replace", index=False
)

# Save outliers db data from the transform complex script file
outliers = df.filter(pl.col("outlier_flag")).select(
    ["category", "quantity", "mean_quantity", "outliers_std_deviations", "outlier_flag"]
)

outliers.to_pandas().to_sql("outliers", conn, if_exists="replace", index=False)

# Close the connection
conn.close()

print(f"Data successfully stored in SQLite database: {DB_FILE.name}")

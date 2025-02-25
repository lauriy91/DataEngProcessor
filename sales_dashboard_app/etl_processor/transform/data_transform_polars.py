import polars as pl
from pathlib import Path

# Roots
DATA_DIR = Path("sales_dashboard_app/data")
INPUT_FILE = DATA_DIR / "cleaned_data.csv"
OUTPUT_FILE = DATA_DIR / "transformed_data.csv"

df = pl.read_csv(INPUT_FILE)

# Derived Columns
df = df.with_columns(pl.col("date").str.strptime(pl.Date, "%Y-%m-%d"))
df = df.with_columns(
    [
        (pl.col("quantity") * pl.col("price")).alias("total_sales").round(2),
        (pl.col("date").dt.strftime("%A")).alias("day_of_week"),
        (pl.col("quantity") > 10.0).alias("high_volume"),
    ]
)

# Save the transformed file
df.write_csv(OUTPUT_FILE)
print(f"Data processing completed. Transformed file saved as: {OUTPUT_FILE.name}")

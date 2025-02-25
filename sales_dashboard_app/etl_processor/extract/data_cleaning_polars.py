import polars as pl
from pathlib import Path

# Roots
DATA_DIR = Path("sales_dashboard_app/data")
INPUT_FILE = DATA_DIR / "data_sales.csv"
OUTPUT_FILE = DATA_DIR / "cleaned_data.csv"

df = pl.read_csv(INPUT_FILE)

# Handle missing values and fill in missing values
df = pl.read_csv(INPUT_FILE, null_values="")
df = df.with_columns(pl.col("quantity").fill_null(0))

# Calculate median price and Replace missing with median price
df = pl.read_csv("sales_dashboard_app/data/data_sales.csv", null_values="not_a_number")

category_median_price = df.group_by("category").agg(
    pl.col("price").mean().alias("median")
)

# Replace missing with median price
df = df.join(category_median_price, on="category", how="left")
df = df.with_columns(
    pl.when(pl.col("price").is_null())
    .then(pl.col("median"))
    .otherwise(pl.col("price"))
    .alias("price")
    .round(2)
)

# Save the cleaned file
df = df.drop("median")
df = df.filter(~(pl.col("quantity").eq(0) & pl.col("price").is_null()))
df.write_csv(OUTPUT_FILE)
print(f"Data cleaned and saved as: {OUTPUT_FILE.name}")

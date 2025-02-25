import polars as pl
from pathlib import Path

# Roots
DATA_DIR = Path("sales_dashboard_app/data")
INPUT_FILE = DATA_DIR / "transformed_data.csv"
OUTPUT_FILE = DATA_DIR / "transformed_complex_data.csv"

df = pl.read_csv(INPUT_FILE)

# Identify category metrics in the data
category_metrics_group = df.group_by("category").agg([
    pl.col("price").mean().alias("average_price"),
    pl.col("total_sales").sum().alias("total_revenue"),
    pl.col("date").mode().first().alias("day_with_highest_sales")
])

# Identify outliers in the data
category_outliers_data = df.group_by("category").agg([
    pl.col("quantity").mean().alias("mean_quantity"),
    pl.col("quantity").std().alias("outliers_std_deviations"),
])

# Merge added metrics with the original dataframe
df = df.join(category_metrics_group, on="category", how="left")
df = df.join(category_outliers_data, on="category", how="left")

standar_quantity = (pl.col("quantity") - pl.col("mean_quantity"))
df = df.with_columns((standar_quantity.abs() > 2 * pl.col("outliers_std_deviations")).alias("outlier_flag"))
print("df =", df)

# Save the transformed file
df.write_csv(OUTPUT_FILE)
print(f"Data processing completed. Transformed file saved as: {OUTPUT_FILE.name}")
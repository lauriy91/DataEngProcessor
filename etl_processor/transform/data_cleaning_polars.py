import polars as pl

# Handle missing values and fill in missing values
df = pl.read_csv("etl_processor/data/data_sales.csv", null_values="")
df = df.with_columns(pl.col("quantity").fill_null(0))

# Calculate median price and Replace missing with median price
df = pl.read_csv("etl_processor/data/data_sales.csv", null_values="not_a_number")

category_median_price = df.group_by("category").agg(pl.col("price").mean().alias("median"))

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
data_cleaned = "transformed_data.csv"
df.write_csv(f"etl_processor/data/{data_cleaned}")

print(f"data cleaned and saved as: {data_cleaned}")
import polars as pl

df = pl.read_csv("etl_processor/data/cleaned_data.csv")
                                                 
# Derived Columns
df = df.with_columns(pl.col("date").str.strptime(pl.Date, "%Y-%m-%d"))
df = df.with_columns([
    (pl.col("quantity") * pl.col("price")).alias("total_sales").round(2),
    (pl.col("date").dt.strftime("%A")).alias("day_of_week"),
    (pl.col("quantity") > 10.0).alias("high_volume")
])

# Save the tranformed file
df.write_csv("etl_processor/data/transformed_data2.csv")
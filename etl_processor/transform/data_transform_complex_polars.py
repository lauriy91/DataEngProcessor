import polars as pl

df = pl.read_csv("etl_processor/data/transformed_data.csv")

# Group data by category and calculate
category_group = df.group_by("category").agg([
    pl.col("price").mean().alias("average_price"),
    pl.col("total_sales").sum().alias("total_revenue"),
    pl.col("date").mode().alias("day_with_highest_sales")  # Modo para obtener el día más frecuente de ventas
])

# Identify outliers in the data
category_outliers_data = df.group_by("category").agg([
    pl.col("quantity").mean().alias("mean_quantity"),
    pl.col("quantity").std().alias("std_quantity"),
])
df = df.join(category_outliers_data, on="category", how="left")

standar_quantity = (pl.col("quantity") - pl.col("mean_quantity"))

df = df.with_columns((standar_quantity.abs() > 2 * pl.col("std_quantity")).alias("outlier_flag"))

# Save the transformed file
data_trasnformed = "transformed_complex_data.csv"
df.write_csv(f"etl_processor/data/{data_trasnformed}")
print(f"data transformed and saved as: {data_trasnformed}")
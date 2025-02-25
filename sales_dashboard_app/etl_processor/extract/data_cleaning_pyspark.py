from pyspark.sql import SparkSession
from pyspark.sql.functions import col, median, when

spark = SparkSession.builder.appName("DataCleaning").getOrCreate()
df = spark.read.csv("etl_processor/data/data_sales.csv", header=True, inferSchema=True)

# Handle missing values and fill in missing values
df = df.fillna({"quantity": 0})

# Calculate median price and Replace missing with median price
median_price_by_category = df.groupBy("category").agg(
    median("price").alias("median_price")
)
df = (
    df.join(median_price_by_category, "category", "left")
    .withColumn(
        "price",
        when(col("price").isNull(), col("median_price")).otherwise(col("price")),
    )
    .drop("median_price")
)
df = df.filter(~((col("quantity") == 0) & col("price").isNull()))

df.show()
df.write.csv("etl_processor/data/cleaned_data.csv", header=True, mode="overwrite")

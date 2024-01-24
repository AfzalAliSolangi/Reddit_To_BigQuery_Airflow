import io
import pandas as pd
import requests
from datetime import datetime
from google.cloud import storage,bigquery
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum
from pyspark.sql.types import IntegerType, TimestampType, FloatType, BooleanType


# spark = SparkSession.builder.appName("PySparkTest").config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery_2.12:0.23.0").getOrCreate()



client = bigquery.Client(project = 'academic-pier-405912')

distinct_file_name ='reddit_{}'.format(datetime.now().strftime("%Y%m%d"))  #File name present in the bucket with date
bucket_name = 'afzal03082821k407711123' 
file_name = 'raw_data/{}.tsv'.format(distinct_file_name)  #Replace with the actual file path in the bucket.
jar_file_path = 'gs://{}/spark-3.5-bigquery-0.35.1.jar'.format(bucket_name)



# Create a Spark session
# spark = SparkSession.builder.appName("PySparkTest").getOrCreate()
spark = SparkSession.builder.appName("PySparkTest").getOrCreate()

#Reading spark file
df = spark.read.option("header","true").option("sep", "\t").option("multiLine", "true").option("quote","\"").option("escape","\"").option("ignoreTrailingWhiteSpace", "true").csv('gs://' + bucket_name + '/' + file_name)

#Converting the data types
df = df.withColumn("id", col("id").cast("string"))
df = df.withColumn("created_utc", col("created_utc").cast(TimestampType()))
df = df.withColumn("url", col("url").cast("string"))
df = df.withColumn("author", col("author").cast("string"))
df = df.withColumn("upvote_ratio", col("upvote_ratio").cast(FloatType()))
df = df.withColumn("num_comments", col("num_comments").cast(IntegerType()))
df = df.withColumn("stickied", col("stickied").cast(BooleanType()))
df = df.withColumn("score", col("score").cast(IntegerType()))
df = df.withColumn("spoiler", col("spoiler").cast(BooleanType()))
df = df.withColumn("title", col("title").cast("string"))
df = df.withColumn("over_18", col("over_18").cast(BooleanType()))
df = df.withColumn("edited", col("edited").cast(BooleanType()))
df = df.withColumn("selftext", col("selftext").cast("string"))


#Reording the columns according the BigQuery Table
column_order = [
    "id", "created_utc", "url", "author", "upvote_ratio",
    "num_comments", "stickied", "score", "spoiler",
    "title", "over_18", "edited", "selftext"
]
df_reordered = df.select(column_order)


# Loading the data into the table
table_id = 'academic-pier-405912.testdataset20240115.Reddit4'

#Printing after reading file
df_reordered = df_reordered.toPandas()

job_config = bigquery.LoadJobConfig(
write_disposition = 'WRITE_APPEND')

job = client.load_table_from_dataframe(
    df_reordered,table_id,job_config=job_config
)
job.result()
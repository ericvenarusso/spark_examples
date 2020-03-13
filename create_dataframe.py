from yspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder \
                    .appName("Teste")
                    .getOrCreate()

rows = [
  {
    'name': 'Alice', 
    'age': 1
  },
  {
    'name': 'Eric', 
    'age': 2
  },
  {
    'name': 'Lucas', 
    'age': 3
  }
]

df = spark.createDataFrame(rows)

print(df.show())

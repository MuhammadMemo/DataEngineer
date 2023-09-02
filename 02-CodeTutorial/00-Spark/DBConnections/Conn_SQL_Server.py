
# Enable IP-TCP in sql server config
# 

from pyspark.sql import SparkSession

from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, IntegerType, BinaryType, LongType

spark = SparkSession\
    .builder\
    .appName("Sql_Server")\
    .master("yarn")\
    .config("spark.yarn.queue", "prod")\
    .config("spark.driver.extraClassPath","/home/hadoop/spark-3.4.1-bin-hadoop3/jars/mssql-jdbc-12.2.0.jre8.jar")\
    .getOrCreate()

jdbc_url = "jdbc:sqlserver://192.168.1.200:1433;database=dynamicsax1;integratedSecurity=false;trustServerCertificate=true;"
connection_details = { "user": "sa", "password": "P@ssw0rd", "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver", }
df = spark.read.jdbc(url=jdbc_url, table="dbo.salesline", properties=connection_details)
df.show()

#-----------------------------------OR-------------------------------------

from pyspark import SparkContext, SparkConf, SQLContext

# conf = SparkConf() \
#     .setAppName("Sql_Server") \
#     .setMaster("yarn") \
#     .set("spark.yarn.queue", "prod")\
#     .set("spark.driver.extraClassPath","/home/hadoop/spark-3.4.1-bin-hadoop3/jars/mssql-jdbc-12.2.0.jre8.jar")
# sc = SparkContext(conf=conf)
# sqlContext = SQLContext(sc)
# spark = sqlContext.sparkSession


# df = spark.read.format("jdbc")\
#   .option("url", "jdbc:sqlserver://192.168.1.200:1433;database=dynamicsax1;integratedSecurity=false;trustServerCertificate=true;") \
#   .option("dbtable", "dbo.salesline")\
#   .option("user", "sa") \
#   .option("password", "P@ssw0rd")\
#   .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
#   .load()

# df.show()
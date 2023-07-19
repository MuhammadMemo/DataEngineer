#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyspark


# In[ ]:


import findspark
findspark.init()
findspark.find()
import pyspark
findspark.find()


# In[ ]:


# Import PySpark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder.appName('my app').getOrCreate()

# Data
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

# Columns
columns = ["language","users_count"]


# Create DataFrame
df = spark.createDataFrame(data).toDF(*columns)

# Print DataFrame
df.show()


# In[ ]:


import os
import sys

os.environ['C:\\Users\\Tech Shop\AppData\\Local\\Programs\\Python\\Python311\\Scripts'] = sys.executable
print("d")


# In[ ]:


import findspark
findspark.init('C:\\Spark\\spark-3.4.0-bin-hadoop3')
import pyspark
sc = pyspark.SparkContext()
print ('f')


# In[ ]:





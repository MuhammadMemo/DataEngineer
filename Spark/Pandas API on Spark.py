#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys

#os.environ['C:\\Users\\Tech Shop\AppData\\Local\\Programs\\Python\\Python311\\Scripts'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON_OPTS']= "notebook"
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"


# In[2]:


import pandas as pd
import numpy as np
import pyspark.pandas as ps
from pyspark.sql import SparkSession


# In[ ]:


dataLoad=ps.read_csv("F:\\fact100.txt")
psdf = ps.DataFrame(dataLoad)


# In[4]:


psdf


# In[5]:


spark = SparkSession.builder.getOrCreate()


# In[6]:


sdf = spark.createDataFrame(psdf)


# In[34]:


df = spark.createDataFrame([], 'a INT, b DOUBLE, c STRING')  # works!
df.dtypes


# In[ ]:





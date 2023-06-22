#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys

os.environ['C:\\Users\\Tech Shop\AppData\\Local\\Programs\\Python\\Python301\\Scripts'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON_OPTS']= "notebook"
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['PYSPARK_PYTHON'] = sys.executable


# In[3]:


from pyspark import SparkContext,SparkConf


# In[ ]:


conf = SparkConf().setMaster("local").setAppName("Myapp")


# In[ ]:


sc = SparkContext(conf = conf)


# In[ ]:


line=sc.textFile("F:\\fact100.txt")


# In[ ]:


line


# In[ ]:


line.collect()


# In[ ]:


line.count()


# In[ ]:


line.countByValue()


# In[1]:


import sys
print(sys.executable)
print(sys.version)
print(sys.version_info)


# In[ ]:





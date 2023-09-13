import json
import facebook
import requests
import numpy as np
import pandas as  pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from arabicstopwords.stopwords_lexicon import stopwords_lexicon 
import arabicstopwords.arabicstopwords as stp
import pyarabic.arabrepr
from tashaphyne.stemming import ArabicLightStemmer
import re

spark = SparkSession\
        .builder\
        .appName("facebook_Data")\
        .master("local")\
        .config("spark.yarn.queue","prod")\
        .config("hive.metastore.uris", "thrift://localhost:9084")\
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse")\
        .config("spark.sql.catalogImplementation", "hive")\
        .enableHiveSupport()\
        .getOrCreate()
spark   
      
df_p=spark.read.parquet('hdfs://localhost:9000/user/hive/lake/01-posts_p.parquet')
df_p.show(truncate=False)
df_p.count()
df_c=spark.read.parquet('hdfs://localhost:9000/user/hive/lake/02-Comments_p.parquet')
df_c.show(truncate=False)
df_c.count()

comments_message=df_c.toPandas()
comments_message=comments_message['comments_message']
comments_message

listText=[]
for i in comments_message:
   listText.append(i)
   
comments=df_c.toPandas()

wcss=[]
# Convert text data to numerical vectors using TF-IDF
vectorizer = TfidfVectorizer()
data_vectors = vectorizer.fit_transform(listText)
for i in  range(10,31):
    Kmeans=KMeans(n_clusters=i,init='k-means++',random_state=45)
    Kmeans.fit(data_vectors)
    wcss.append(Kmeans.inertia_)


plt.plot(range(10,31),wcss)
plt.title("The Elbow Mathod")
plt.xlabel("Number of Clusters")
plt.ylabel("wcss")
plt.show()

Kmeans=KMeans(n_clusters=4,init='k-means++',random_state=45)
yKmeans=Kmeans.fit_predict(data_vectors)

comments['Clustering']=yKmeans
comments.head(10)

comments.groupby(['Clustering'])['Clustering'].count()


corpus=[]
for i in range(1,len(listText)):
    review=re.sub('[^ء-ي]', ' ' , listText[i] ) 
    review=review.split()
    review= [x for x in review  if not x in stp.stop_stem(x)]
    review=' '.join(review)
    corpus.append(review)
corpus

yText=comments['Clustering']
y=[]
for i in yText:
   y.append(i)
   
cv=CountVectorizer()
x=cv.fit_transform(corpus).toarray()
x = vectorizer.fit_transform(listText)

from sklearn.model_selection import train_test_split
x_trine,x_test,y_trine,y_test=train_test_split(x,y,test_size=.2,random_state=0)

from sklearn.ensemble import  RandomForestClassifier
Classifier=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
Classifier.fit(x_trine,y_trine)

y_pred=Classifier.predict(x_test)
len(y_pred)

comments['y_pred']=y_pred
comments.head(50)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
cm

# Combine the test data and predicted labels into a DataFrame
df_results = pd.DataFrame({'Test Data': y_test, 'Predicted Label': y_pred})
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
# Print the DataFrame
df_results.head(50)
import json
import facebook
import requests
import numpy as np
from pyspark.sql import SparkSession

def ConnectAPI():
    access_token='EAAKh3aJk1o4BOzzQx2hDoMwawGGymavLOd1W9XGyqlaBZBPvWxBIEqlOnldZBxPk1AalXh3ll9ZCxVaQK6UM2ADFBj9AqeJp4y9QtcRE4XZB7GIRxsE6eeHYZCpOhth42RXKr0liESOhRbCsCLwSOVAe8jukr500LbyZBRHzbSCgP5q5B3XPu4pVlZBtSfQAkbD'
    page_id='365304090334712'
    url = f'https://graph.facebook.com/v17.0/{page_id}/posts?fields=id,message,created_time,permalink_url,full_picture,likes.limit(0).summary(true),comments{{id,message,created_time}}&access_token={access_token}'
    return url

# Extract data from the response data
def get_Data(url):
    data=[]
    response = requests.get(url)
    data = response.json()

    postslist=[]   
    commentslist=[]
    posts = data['data']
    while 'paging' in data and 'next' in data['paging']:
        next_url = data['paging']['next']
        response = requests.get(next_url)
        data=response.json()
        posts.extend(data['data'])


    for post in posts:        
        id=post['id']
        message=post.get('message', '')
        created_time=post['created_time']
        full_picture=post.get('full_picture', '')
        permalink_url=post['permalink_url']
        likes=post['likes']['summary']['total_count']
        postslist.extend((id,message,created_time,full_picture,permalink_url,likes))

    # # Extract comments
        if 'comments' in post:
            comments = post['comments']['data']
            for comment in comments:
                id=post['id']
                comments_id=comment['id']
                comments_message=comment.get('message', '')
                comments_created_time=comment['created_time']
                commentslist.extend((id,comments_id,comments_created_time,comments_message))
    return postslist,commentslist

def write_Post(postslist):
    arr_p = np.array(postslist)
    lenarry = int((len(arr_p))/6)
    arr_posts = arr_p.reshape(lenarry,6)
    schema=['id','message','created_time','full_picture','permalink_url','likes']
    df_posts = spark.createDataFrame(data=arr_posts,schema=schema)
    df_posts.repartition(1).write.parquet('hdfs://localhost:9000/user/hive/lake/01-posts_p.parquet',mode='overwrite')
    df_posts.printSchema()
    return True

def write_Comments(commentslist):
    arr_c = np.array(commentslist)
    lenarry = int((len(arr_c))/4)
    arr_Comments = arr_c.reshape(lenarry,4)
    schema=['id','comments_id','comments_created_time','comments_message']
    df_comments = spark.createDataFrame(data=arr_Comments,schema=schema)
    df_comments.repartition(1).write.parquet('hdfs://localhost:9000/user/hive/lake/02-Comments_p.parquet',mode='overwrite')
    df_comments.printSchema()
    return True

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("facebook")\
        .master("local")\
        .config("spark.yarn.queue","prod")\
        .config("hive.metastore.uris", "thrift://localhost:9084")\
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse")\
        .config("spark.sql.catalogImplementation", "hive")\
        .enableHiveSupport()\
        .getOrCreate()
    spark   

            
    Connect=ConnectAPI()
    postslist,commentslist= get_Data(Connect) 
    write_Post(postslist)
    write_Comments(commentslist)
    

    
    
    
    
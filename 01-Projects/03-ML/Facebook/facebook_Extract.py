import json
import facebook
# import pandas as pd
import numpy as np
from pyspark.sql import SparkSession

def ConnectAPI():
    Access_Token='EAAKh3aJk1o4BOzzQx2hDoMwawGGymavLOd1W9XGyqlaBZBPvWxBIEqlOnldZBxPk1AalXh3ll9ZCxVaQK6UM2ADFBj9AqeJp4y9QtcRE4XZB7GIRxsE6eeHYZCpOhth42RXKr0liESOhRbCsCLwSOVAe8jukr500LbyZBRHzbSCgP5q5B3XPu4pVlZBtSfQAkbD'
    mffco_page_id='365304090334712'
    graph = facebook.GraphAPI(Access_Token)
    fields='posts{message,id,created_time,likes.limit(0).summary(true),comments{id,message,created_time},full_picture,permalink_url}, limit=100'
    page = graph.get_object(id=mffco_page_id,fields=fields)
    return page

def LoadData(page):
    readjson = json.dumps(page)
    json_data = json.loads(readjson)
    return json_data

def Posts(json_data):
    postslist=[]
    for i in json_data['posts']['data']:
        for r in i:
            if r == 'message':
                message= i['message']
            elif r == 'story' : message = i['story']
        id=i['id']
        created_time=i['created_time']
        full_picture=i['full_picture']
        permalink_url=i['permalink_url']
        likes=i['likes']['summary']['total_count']
        postslist.extend((id,message,created_time,full_picture,permalink_url,likes))
        
    arr_p = np.array(postslist)
    lenarry = int((len(arr_p))/6)
    arr_posts = arr_p.reshape(lenarry,6)
    columens=['id','message','created_time','full_picture','permalink_url','likes']
    df_posts = spark.createDataFrame(data=arr_posts,schema=columens)
    df_posts.repartition(1).write.csv('/home/hadoop/SparkProjects/Facebook/01-posts.csv',mode='overwrite',header=True)

def comments(json_data):
    commentslist=[]
    for i  in json_data['posts']['data']:
        try :
            comments= i['comments']
            for n in comments['data']:
                    id=i['id']
                    comments_id=n['id']
                    comments_message=n['message']
                    comments_created_time=n['created_time']
                    commentslist.extend((id,comments_id,comments_created_time,comments_message))
        except: 
            "no"
    arr_c = np.array(commentslist)
    lenarry = int((len(arr_c))/4)
    arr_Comments = arr_c.reshape(lenarry,4)
    columens=['id','comments_id','comments_created_time','comments_message']
    df_comments = spark.createDataFrame(data=arr_Comments,schema=columens)
    df_comments.repartition(1).write.csv('/home/hadoop/SparkProjects/Facebook/02-Comments.csv',mode='overwrite',header=True)    
            
if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("facebook")\
        .master("yarn")\
        .config("hive.metastore.uris", "thrift://localhost:9084")\
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse")\
        .config("spark.sql.catalogImplementation", "hive")\
        .enableHiveSupport()\
        .config("spark.yarn.queue","prod")\
        .getOrCreate()
    spark
    
    
    page= LoadData(ConnectAPI())
    Posts(LoadData(page)) 
    comments(LoadData(page))
    print("Done")

# import requests
# token='EAAKh3aJk1o4BO43tNPLgSIKWJ4HWZBZBaZAoC1ClCSnUomZCQTYG6fdrhTEF8mUa8NqGDni3VSsyhy89lZBGkyjTkNfszubPQ75HwYnn7mfD4bL3r2ZBZBPZBexckGeWaUPDZBpwliHcays6MEokRzT4h0FmHyDCVUqk05j8sOaYhM4TZAWeV632bVxhDw4ZAZCLrYjH6fLtZCaC5ivHmkSZBwtoFdCjVhxqLbfGlpeGxNVeeczYZACZCaC1mwibooJjfeTadgZDZD'
# graph = facebook.GraphAPI(access_token=token, version = 17.0)
# events = graph.request('/search?q=Poetry&type=event&limit=10000')
# print(events)
# curl = "https://graph.facebook.com/v17.0/me?fields=id%2Cname%2Cemail%2Cevents%7Bname%2Cposts.limit(10)%2Ccomments.limit(10)%7D&access_token=EAAKh3aJk1o4BO9af1NZC1XgntmaJGFHt43CL9LqnexU36xu56BP0yLC4TtLDhWfeJUEktEtW9heJBVKeMUZBWWtLG5AlF4HgCZBW1ZAUe7WqrorpAvXWwm9piNW5HQuhLCQLV6BKC7e07suvJL6vtKgcWyGPlFOBQXrqgJNlRzXqZAXqdD2JEVSSDCO18DeoLzcEtzzVZCQdCayV3DUaJtrpZCW4Q5CbnAnk21ssjppZBnTVZAvYtZA8VVm2PkFTp7vwZDZD"
# res=requests.get(curl)
# print(res.text)

# Posts = parse('posts[*].data[*].[id,created_time,message,story]')
# Posts_id = parse('posts[*].data[*].id')
# Comments = parse('posts[*].data[*].comments[*].data[*].[id,created_time,message]')
# Posts_id = parse('posts[*].data[*].[id]')
# Posts_id.find(json_data)

# Posts_fields= Posts.right.fields
# Comments_fields=Comments.right.fields
# Posts_field_id= Posts_id.right.fields
# print(Posts.filter(json_data['id']))
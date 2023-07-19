

import mysql.connector
Myconn=mysql.connector.connect(host="Localhost",user="root",password ="P@ssw0rd" ,
                              auth_plugin='mysql_native_password',database='mydbtest')
mysqlcorsr=Myconn.cursor()
""" if (mysqlcorsr.execute("create database MyDBTest")):
    print("Done") """

# mysqlcorsr.execute("create table MtTable (name  varchar (50),id int(20))")
# print("Done")
#mysqlcorsr.execute("insert into mttable (name,id) values ('Muhammad',1)")

#Myconn.commit()

mysqlcorsr.execute("select * from MtTable")
myresult=mysqlcorsr.fetchall()

# for i in myresult:
#     print(i)

# myresult.clear()

# print(myresult)
#print(Myconn)
#print("ddddd")

import pandas as ps
df=ps.DataFrame(myresult)
df.rename(columns={0:"Nmae",1:"ID"},inplace=True)

print(df)
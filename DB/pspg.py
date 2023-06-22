
import psycopg2 
""" pgConn=psycopg2.connect(host="localhost",user="openpg",password="P@ssw0rd",database="RetailDB",port=5432)

pgCursr=pgConn.cursor()

pgCursr.execute("SELECT * FROM sale_order_line LIMIT 100")
pgResult=pgCursr.fetchall()

pgConn.close()

import pandas as ps

ps.set_option('display.expand_frame_repr', False);
df=ps.DataFrame(pgResult)
#df.rename(columns={0:"Nmae",1:"ID"},inplace=True)
df.to_csv("PG.csv",header=True)
print(df)  """


""" 
Microsoft SQL Server: “mssql+pyodbc://username:password@host:port/database”
MySQL: “mysql+mysqlconnector://username:password@host:port/database”
PostgreSQL: “postgresql+psycopg2://username:password@host:port/database”
 """

from sqlalchemy import create_engine
import pg8000
# Create an engine instance
#'postgresql://user@localhost:5432/mydb




alchemyEngine = create_engine("postgresql+psycopg2://openpg:P@ssw0rd@localhost:5432/RetailDB");
# Connect to PostgreSQL server
print(alchemyEngine)
dbConnection = alchemyEngine.connect();

# Read data from PostgreSQL database table and load into a DataFrame instance
df2   = ps.read_sql("select * from \"StudentScores\"", dbConnection);
ps.set_option('display.expand_frame_repr', False);

# Print the DataFrame

print(df2);
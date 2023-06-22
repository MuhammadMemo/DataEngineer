
import psycopg2 
import pandas as ps
from sqlalchemy import create_engine
from sqlalchemy import URL

url_object = URL.create(
    "postgresql+psycopg2",
    username="openpg",
    password="P@ssw0rd",  # plain (unescaped) text
    host="localhost",
    database="RetailDB",
)

#alchemyEngine = create_engine("postgresql+psycopg2://openpg:P@ssw0rd@localhost:5432/RetailDB");

alchemyEngine = create_engine(url_object);
# Connect to PostgreSQL server
print(alchemyEngine)
dbConnection = alchemyEngine.connect();

# Read data from PostgreSQL database table and load into a DataFrame instance
df2   = ps.read_sql("SELECT * FROM sale_order_line LIMIT 100", dbConnection);
ps.set_option('display.expand_frame_repr', False);

# Print the DataFrame

print(df2);
df2.to_csv("sale_order_line.csv",header=True)
#------------------
pgConn=psycopg2.connect(host="localhost",user="openpg",password="P@ssw0rd",database="RetailDB",port=5432)

pgCursr=pgConn.cursor()

pgCursr.execute("SELECT * FROM sale_order_line LIMIT 100")
pgResult=pgCursr.fetchall()

pgConn.close()



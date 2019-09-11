#POSTGRES SQL
import psycopg2 

#My config
from config import DATABASE
from config import USER
from config import HOST
from config import PASSWORD


conn = psycopg2.connect(database=DATABASE,
                        user=USER,
                        host=HOST,
                        password=PASSWORD) 
cur = conn.cursor()

#sql ask
cur.execute("""ALTER TABLE Immobilier ALTER COLUMN long type decimal(10,2);
            """)

conn.commit() 

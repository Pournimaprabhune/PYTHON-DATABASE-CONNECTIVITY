import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
try:
     cur.execute("delete from customers where id ='103'")
     conn.commit()
except:
       conn.rollback()
conn.close() 
           
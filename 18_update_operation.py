import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
try:
    cur.execute("update customers set name='alex' where id='102'")
    conn.commit()
except:
     conn.rollback()
conn.close()     
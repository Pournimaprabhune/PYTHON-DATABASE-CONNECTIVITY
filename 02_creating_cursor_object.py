import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='pournima')
print(conn)
cur=conn.cursor()
print(cur)
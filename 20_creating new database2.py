import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123')
cur=conn.cursor()
try:
    cur.execute("create database mydb")
    dbs=cur.execute("show databases")
except:
      conn.rollback()

for x in cur:
         print(x)

conn.close()         

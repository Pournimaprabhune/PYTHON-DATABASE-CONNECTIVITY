import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
try:
     cur.execute("select name,id,salary from customers order by name")
     result=cur.fetchall()
     print("name id salary")

     for x in result:
           print("%s %d %d"%(x[0],x[1],x[2]))

except:
       conn.rollback()

conn.close()       
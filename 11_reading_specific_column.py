import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
try:
    cur.execute("select name,id,salary from customers")
    result=cur.fetchall()

    for x in result:
        print(x)
except:

    conn.rollback()

conn.close()
    
import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
try:
    #reading employee data
    cur.execute("select * from customers")

    #fetching the rows from the cursor object
    result=cur.fetchall()

    #printing the result
    for x in result:
                 print(x)
except:
        conn.rollback()

conn.close()        
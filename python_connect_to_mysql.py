import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='pournima')
my_curser=conn.cursor()
conn.commit()
conn.close()
print("connection successfully created")

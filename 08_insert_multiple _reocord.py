import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
sql="insert into customers(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val=[('pournima',104,220000,204,'newyork'),('anushree',102,27000,202,'india'),('samu',103,30000,203,'america')]
cur.executemany(sql,val)

conn.commit()

print(cur.rowcount,"record inserted")  
 
conn.close()

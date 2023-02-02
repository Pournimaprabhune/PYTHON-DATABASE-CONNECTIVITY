import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='mydb')
cur=conn.cursor()
sql="insert into employee(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val=[('anu',101,25000,301,'pune'),('samu',102,26000,302,'katraj'),('komal',103,24000,303,'mumbai'),('vishwa',104,28000,304,'delhi')]
cur.executemany(sql,val)
sql1="insert into departments(dept_id,dept_name)values(%s,%s)"
val1=[(302,'CS'),(303,'IT')]
cur.executemany(sql1,val1)
conn.commit()

print(cur.rowcount,"record inserted")  
 
conn.close()



import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
sql="insert into customers(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val=("mike",105,27000,205,"dattanagar")
try:
   cur.execute(sql,val)
   conn.commit()
except:
     conn.rollback()   
print(cur.rowcount,"record inserted id:",cur.lastrowid)

conn.close()           

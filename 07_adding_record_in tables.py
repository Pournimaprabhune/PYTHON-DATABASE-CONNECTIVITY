import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
sql="insert into customers(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val=("john",101,25000,201,"newyork")
try:
   cur.execute(sql,val)
   conn.commit()
except:
     conn.rollback()   
print(cur.rowcount,"record inserted")

conn.close()           

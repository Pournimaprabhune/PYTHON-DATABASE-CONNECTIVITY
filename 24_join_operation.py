import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='ANUSHREE123',database='mydb')
cur=conn.cursor()
try:
    cur.execute("select employee.id,employee.name,employee.salary,departments.dept_id,departments.dept_name from departments join employee on departments.dept_id=employee.dept_id")
    print("id name salary dept_id dept_name")
    for row in cur:
             print("%d %s %d %d %s"%(row[0],row[1],row[2],row[3],row[4]))

except:
      conn.rollback()
conn.close()   
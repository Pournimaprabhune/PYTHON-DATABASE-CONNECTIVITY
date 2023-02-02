import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
try:
    cur.execute("alter table customers add branch_name varchar(20) not null")
except:
      conn.rollback()
conn.close()          
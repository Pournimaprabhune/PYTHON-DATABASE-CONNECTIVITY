import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='ANUSHREE123',database='pythondb')
cur=conn.cursor()
cur.execute("create table customers(name varchar(20) not null,id int(20) not null primary key,salary float not null,dept_id int not null )")
conn.close()            
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='ANUSHREE123',database='mydb')
cur=conn.cursor()
cur.execute("create table employee(name varchar(20) not null,id int(20) not null primary key,salary float not null,dept_id int not null ,branch_name varchar(20) not null)")
cur.execute("create table departments(dept_id int primary key not null,dept_name varchar(20) not null)")
conn.close()            
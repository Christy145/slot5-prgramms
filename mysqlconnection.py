import mysql.connector
connector=mysql.connector.connect(
    host="localhost",
    user="root",
    password="christy2004",
    database="db_slot5"
)
cursor=connector.cursor()
#cursor.execute("""CREATE TABLE CAMO(ID INT,NAME VARCHAR(50),AGE INT)""")
#cursor.execute("insert into camo values(%s,%s,%s)",(1,"abin",20))
#cursor.execute("insert into camo values(%s,%s,%s)",(2,"appu",30))
#cursor.execute("insert into camo values(%s,%s,%s)",(3,"chris",23))
#connector.commit()
cursor.execute("UPDATE  CAMO SET AGE=25 WHERE ID=1")
connector.commit()
cursor.execute("DELETE FROM CAMO WHERE ID=2")
               
cursor.execute("SELECT * FROM CAMO")
for row in cursor.fetchall():
    print(row)

connector.close()
import mysql.connector
connector=mysql.connector.connect(
    host="localhost",
    user="root",
    password="christy2004",
    database="db_slot5"
)
cursor=connector.cursor()
cursor.execute("""CREATE TABLE categories(ID INT,FOOD VARCHAR(50),TRAVEL VARCHAR(50),SHOPPING VARCHAR(50),BILL VARCHAR(50)""")
cursor.execute("insert into categories (category) values(%s,%s,%s)",(1,"food"))
cursor.execute("insert into categories (category) values(%s,%s,%s)",(2,"travel"))
cursor.execute("insert into categories (category) values(%s,%s,%s)",(3,"shopping"))
cursor.execute("insert into categories (category) values(%s,%s,%s)",(4,"bills"))
connector.commit()
cursor.execute("SELECT * FROM CAMO")
for row in cursor.fetchall():
    print(row)

connector.close()



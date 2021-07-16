import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adam_root",
    database="testdatabase"
)

my_cursor = db.cursor()

#my_cursor.execute("CREATE DATABASE testdatabase")
#my_cursor.execute("CREATE TABLE Person (name  VARCHAR(50), age smallint UNSIGNED, PersonID int PRIMARY KEY AUTO_INCREMENT)")
#my_cursor.execute("DESCRIBE Person")

#my_cursor.execute("INSERT INTO Person (name, age) VALUES ('Jan', 20)")
#db.commit()

my_cursor.execute("SELECT * FROM Person WHERE PersonID=2")

for x in my_cursor:
    print(x)

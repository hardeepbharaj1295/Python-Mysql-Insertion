import mysql.connector
import sys

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="practice7_2"
)

cursor = con.cursor()

def add_customer(tup):
    try:
        cursor.execute("insert into customer(name,email,password) values(%s,%s,%s)",tup)
        con.commit()
        return True
    except:
        print(sys.exc_info())
        return False
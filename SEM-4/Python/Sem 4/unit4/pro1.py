import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="")
print(mydb)
if(mydb):
    print("Connected Successfully")
else:
    print("COnnection FAILED")
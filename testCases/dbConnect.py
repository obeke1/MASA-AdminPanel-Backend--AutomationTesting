import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="classicmodels")

mycursor=conn.cursor()

print("File Load started.....")

mycursor.callproc('SelectAllCustomersByCityAndPin',['singapore','079903',])

for result in mycursor.stored_results():
    rlist=result.fetchall()
    for r in rlist:
        print(r)

conn.close()
import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
print("database connected")

cursor=mydb.cursor()
cursor.execute("DELETE from bhavacopy")
print("table has deleted")
csv_data=csv.reader(open('book1.csv'))
for row in csv_data:
	cursor.execute("INSERT into bhavacopy (SC_CODE,NAME,SC_GROUP,SC_TYPE,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,NO_TRADES,NO_OF_SHRS,NET_TURNOV,TDCLOINDI) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
	print(row)

mydb.commit()
cursor.close()
print('DONE')

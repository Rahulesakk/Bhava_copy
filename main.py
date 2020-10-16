from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route('/')
def index():
	cur=mysql.connection.cursor()

	users=cur.execute("SELECT SC_CODE,NAME,OPEN,HIGH,LOW,CLOSE from bhavacopy limit 10")

	if users>0:
		userdetails=cur.fetchall()
		return render_template('mainpage.html',userdetails=userdetails)

@app.route("/result",methods=["POST","GET"])
def result():
	mycursor = mysql.connection.cursor()
	if request.method=='POST':
		result=request.form
		#print(request.form.'Name')
		name=result['Name']
		#result1=result.upper()
		#name1="'%"+name+"%'"
		mycursor.execute("SELECT SC_CODE,NAME,OPEN,HIGH,LOW,CLOSE from bhavacopy WHERE NAME like %s",["%"+name+"%"])#This is just example query , you should replace field names with yours
		userdetails= mycursor.fetchall()
		#mydb.commit()
		mycursor.close()
		return render_template("mainpage.html", userdetails=userdetails)



if __name__ == '__main__':
    app.run(debug=True)    	
from flask import Flask
from flaskext.mysql import MySQL
import mysql.connector
import MySQLdb
from configparser import SafeConfigParser
#import configparser
from pymysql.cursors import DictCursor

parser = SafeConfigParser()
parser.read('.my.cnf')

app = Flask(__name__)

user = parser.get('client', 'user')
password = parser.get('client', 'password')
database = parser.get('client', 'database')
host = parser.get('client', 'host')
port = parser.get('mysqlId', 'port')

app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = database
app.config['MYSQL_DATABASE_HOST'] = host
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql = MySQL()
mysql.init_app(app)

@app.route("/message", methods=['GET'])
def message():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT message from mytable where 1")
	result =  cursor.fetchone()
	for row in result:
		return row


if __name__ == "__main__":
    app.run(port=5000, threaded=True, host=("0.0.0.0"), debug=True)

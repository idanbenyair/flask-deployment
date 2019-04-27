from flask import Flask
from flaskext.mysql import MySQL
import mysql.connector
import MySQLdb
from ConfigParser import SafeConfigParser
from pymysql.cursors import DictCursor

parser = SafeConfigParser()
parser.read('.my.cnf')

app = Flask(__name__)

user = parser.get('client', 'user')
password = parser.get('client', 'password')
database = parser.get('client', 'database')
host = parser.get('client', 'host')
port = parser.get('mysqlId', 'port')

cnx = mysql.connector.connect(user=user, password=password,
                              host=host,
                              database=database, port=port,
			      auth_plugin='mysql_native_password')
cnx.close()
mysql = MySQL(cnx)

app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = database
app.config['MYSQL_DATABASE_HOST'] = host
app.config['MYSQL_DATABASE_PORT'] = port

mysql.init_app(app)
@app.route("/message")
def message():
    	cursor = mysql.connect().cursor()
    	return cursor.fetchone()


if __name__ == "__main__":
    app.run(port=5000, threaded=True, host=("0.0.0.0"))

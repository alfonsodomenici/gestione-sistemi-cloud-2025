from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
cors = CORS()
cors.init_app(app ,resources={r"/*": {"origins":"*"}})

db = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'db25_prova'
db.init_app(app)

@app.route("/registration")
def registration():
    return "Registration endpoint"
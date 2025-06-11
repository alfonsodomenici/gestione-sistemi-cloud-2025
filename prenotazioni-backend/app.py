from flask import Flask,request,json, Response
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
app.config['MYSQL_CURSORCLASS']="DictCursor"
db.init_app(app)

@app.route("/registration")
def registration():
    print("Registration endpoint hit")
    return Response(json.dumps({"message": "Registration endpoint"}), status=200, mimetype='application/json')


def testdb():
    try:
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM t_user ")
        results = cursor.fetchall()
        return Response(json.dumps(results), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), mimetype='application/json')@app.route("/testdb")
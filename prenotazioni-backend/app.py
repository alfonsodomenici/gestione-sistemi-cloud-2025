from flask import Flask,request,json, Response
from flask_cors import CORS
from flask_mysqldb import MySQL
from http import HTTPStatus

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

@app.route("/registration", methods=['POST'])
def registration():
    firstname,lastname,phone, mail,pwd =  request.json.values()
    q = f"""
        insert into t_user (firstname,lastname,phone,mail,pwd) 
        values ('{firstname}','{lastname}','{phone}','{mail}','{pwd}')
        """
    conn = db.connection
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    lastid = cursor.lastrowid
    return Response(json.dumps({"id": lastid}), mimetype='application/json')

@app.route("/login", methods=['POST'])
def login():
    mail, pwd = request.json.values()
    q = f"""
        select id_user as id,mail from t_user where mail='{mail}' and pwd='{pwd}'
        """
    cursor = db.connection.cursor()
    cursor.execute(q)
    user = cursor.fetchone()
    if user:
        return Response(json.dumps(user), mimetype='application/json')
    else:
        return Response(response="login failed", status=HTTPStatus.FORBIDDEN, content_type='text/plain')

@app.route("/prenotazioni/<int:user_id>")
def prenotazioni(user_id):
    try:
        cursor = db.connection.cursor()
        q = f"SELECT * FROM t_prenotazione WHERE id_user={user_id}"
        cursor.execute(q)
        results = cursor.fetchall()
        return Response(json.dumps(results), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), mimetype='application/json')
    

@app.route("/test")
def testdb():
    try:
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM t_user ")
        results = cursor.fetchall()
        return Response(json.dumps(results), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), mimetype='application/json')@app.route("/testdb")
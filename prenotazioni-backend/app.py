from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS()
cors.init_app(app ,resources={r"/*": {"origins":"*"}})

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
from flask import Flask, make_response, jsonify, request, current_app
from flask_mysqldb import MySQL
from functools import wraps
import xmltodict

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "db_myhotel"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["SITE_USER"] = "larry"
app.config["SITE_PASS"] = "12345"

mysql = MySQL(app)


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

#authentication
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if (
            auth
            and auth.username == current_app.config["SITE_USER"]
            and auth.password == current_app.config["SITE_PASS"]
        ):
            return f(*args, **kwargs)
        return make_response(
            "<h1>Access denied!</h1>",
            401,
            {"WWW-Authenticate": 'Basic realm="Login required!"'},
        )

    return decorated

#welcome-page
@app.route("/")
@auth_required
def Welcome_page():
    return "<p>Welcome to My Final Drill. My name is Larry John</p>"



if __name__ == "__main__":
    app.run(debug=True)
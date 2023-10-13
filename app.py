from flask import Flask, render_template, url_for, session, request, redirect
import os
import constants

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = str(os.urandom(20).hex())
@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html", autors=constants.AUTORS)
@app.route('/whoami.html', methods=["GET", "POST"])
def whoami():
    if ("isAutorise" in session):
        return render_template("whoami.html", who=constants.WHOAMI, ads=constants.Ads)
    else:
        return render_template("login.html")

@app.post("/login.html")
def login():
    username = request.form.get('username')  # запрос к данным формы
    password = request.form.get('password')
    email = request.form.get("email")
    print(username, password, email)
    session["isAutorise"] = 1
    session["username"] = username
    session["password"] = password
    session["email"] = email
    return redirect("whoami.html")


if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, url_for
import constants

app = Flask(__name__)
@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html", autors=constants.AUTORS)

if __name__ == '__main__':
    app.run()
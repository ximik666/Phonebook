__author__ = 'work'
#http://www.syncano.com/intro-flask-pt-2-creating-writing-databases/

import os, sqlite3
from flask import Flask, render_template, send_from_directory, g, request
from models import *
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

@app.route("/signedup", methods=["GET","POST"])
def signedup():

        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        phone = request.form.get('phone')
        insert_account_holder(email,username,phone,password)
        return render_template("homepage.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    return render_template("signup.html")

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')


# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
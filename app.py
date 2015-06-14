__author__ = 'work'
# -*- coding: utf-8 -*-
# ==============
#      Main script file
# ==============
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)
#http://www.syncano.com/intro-flask-pt-2-creating-writing-databases/
# from models import *
import os, sqlite3
from flask import Flask, render_template, send_from_directory, g, request
from models import *
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    DEBUG = True,
)



@app.route("/added", methods=["GET","POST"])
def added():

        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        phone = request.form.get('phone')
        insert_account_holder(email,username,phone,password)
        return render_template("homepage.html")

@app.route("/add", methods=["GET","POST"])
def add():
    return render_template("add.html")

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.route("/test")
def test():
    contacts = select_by_all()
   # print contacts
    print contacts[1][1]
    for contact in contacts:
        #print contact[0]
        one_c = select_one(contact[0])
        print one_c[0][0]
        #for one in one_c:
           # print one[0]
            #print contact[0]
    return render_template("test.html",contacts=contacts,one_c=one_c)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

def printt():
    print '12'
app.jinja_env.globals.update(printt=printt)

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
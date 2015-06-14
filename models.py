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
import sqlite3 as sql
from app import *

# def insert_account_holder(email, username, phone, password):
#    con = sql.connect("database.db")
#    cur = con.cursor()
#    cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)",
#                (email, username, phone, password))
#    con.commit()
#    con.close()


# def insert_contact(name, phone, username, email):
#    con = sql.connect("database.db")
#    cur = con.cursor()
#    cur.execute("INSERT INTO contact (name,phone,username,email) VALUES (?,?,?,?)", (name, phone, username, email))
#    con.commit()
#    con.close()

def connect_db():
    # """Connects to the specific database."""
    rv = sqlite3.connect('phonebook.db')
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def select_account_holder(params=()):
    con = sql.connect("phonebook.db")
    cur = con.cursor()
    if params == ():
        cur.execute("select * from fio")
    else:
        string = "select"
        for i in xrange(len(params) - 1):
            string += "%s,"
        string += "%s"
        string += " from account_holder"

        result = cur.execute(string)
        con.close()
        return result.fetchall()


# def select_contact(params=()):
#    con = sql.connect("database.db")
#    cur = con.cursor()
#    if params == ():
#        cur.execute("select * from contact")
#    else:
#        string = "select"
#        for i in xrange(len(params) - 1):
#            string += "%s,"
#        string += "%s"
#        string += " from contact"

#        result = cur.execute(string)
#        con.close()
#        return result.fetchall()
def insert_account_holder(email, username, phone, password):
    con = sql.connect("phonebook.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)",
                (email, username, phone, password))
    con.commit()
    con.close()


def select_by_all():
    db = get_db()
    cur = db.execute("select id from fio")
    entries = cur.fetchall()
    return entries

def select_one(id):
    db = get_db()
    #print id
    strin = "select fio from fio where id="+str(id)
    stri = db.execute(strin)
    return stri.fetchall()
def select_one_number(id):
    db = get_db()
    for idd in id:
        strin = "select number,type_number_id from number where fio_id="+str(idd[0])
    return strin

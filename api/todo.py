from flask import Blueprint
from flask import render_template, request, redirect, url_for, jsonify
from flask import g
from . import db
from flask import Flask

import datetime
from flask import render_template, request, redirect, url_for, jsonify, Flask, g, Blueprint
from . import db

bp = Blueprint("todo", "__name__", url_prefix="")


@bp.route("/")   
def main():
  return render_template("login.html")

@bp.route("/login", methods = ["GET", "POST"])
def login():
  conn = db.get_db()
  cursor = conn.cursor()
  status = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    cursor.execute("select id from login l where name = %s and pass=%s ; ", (username,password))
    s= cursor.fetchone()
    if s is None:
        return '''<script>alert("Invalid username or password");window.location='/'</script>'''
    else:
        return redirect(url_for("todo.home",id=s), 302)

    
@bp.route('/logout')
def logout():
    return '''<script>alert("Successfully logged out");window.location='/'</script>'''
@bp.route("/create")
def reg():
  return render_template("register.html")

@bp.route("/register", methods=["POST"])
def register():
  conn = db.get_db()
  cursor = conn.cursor()
  username = request.form['username']
  password = request.form['password']
  cursor.execute("""insert into login (name, pass) values (%s,%s);""", (username, password))
  conn.commit()
  return redirect(url_for("todo.main",), 302)
  
@bp.route("/home/<id>")
def home(id):
  conn = db.get_db()
  cursor = conn.cursor()
  cursor.execute("select * from todolist where uid = %s;",(id))
  s=cursor.fetchall()
  cursor.execute("select name from login where id = %s ;",(id))
  n=cursor.fetchone()
  return render_template("todoform.html",val=s,name=n,id=id)
  
@bp.route("/addtodo/<id>",methods=["POST"])
def addtodo(id):
  conn = db.get_db()
  cursor = conn.cursor()
  task = request.form['todolist']
  date = request.form['date']
  cursor.execute("""insert into todolist (task, lastdate,status,uid) values (%s, %s, FALSE,%s);""", (task, date,id))
  conn.commit()
  return redirect(url_for("todo.home",id=id), 302)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

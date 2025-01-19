import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('movie.html')
@app.route('/createmovie')
def createmovie():
    if request.method=='POST':
        omovie=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table rent(moviename char(17),copy int,customerid int,rentdatetime char(10),returndatetime char(10))')
        cn.close()
        return jsonify('')
@app.route('/addmovie/',methods=['POST','GET'])
def addmovie():
    if request.method=='POST':
        omovie=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=omovie['name']
        copy=omovie['copy']
        cn.execute('insert into movie(name,copy)values(?,?)',(name,copy))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getmovie')
def getmovie():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,copy from movie')
        lmovie=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getmoviecount',methods=['GET','POST'])
def getmoviecount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from movie')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getmovieid')
def getmovieid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,copy from movie where id=?',id)
        omovie=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changemovie',methods=['POST','GET'])
def changemovie():
    if request.method=='POST':
        personal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update movie set name=?,copy=? where id=?',(name,copy))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removemovie',methods=['POST','GET'])
def removemovie():
    movie=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from movie where id=?',(name,copy))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')

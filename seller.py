import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('seller.html')
@app.route('/createseller')
def createseller():
    if request.method=='POST':
        oseller=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table seller(name char(17))')
        cn.close()
        return jsonify('')
@app.route('/addseller/',methods=['POST','GET'])
def addseller():
    if request.method=='POST':
        oseller=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=oseller['name']
        cn.execute('insert into seller( name)values(?)',(name))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getseller')
def getseller():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name from seller')
        lseller=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getsellercount',methods=['GET','POST'])
def getsellercount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from seller')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getsellerid')
def getsellerid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name from seller where id=?',id)
        oseller=cu.fetchall()
        cn.close()
        return jsonify('oseller')
@app.route('/changeseller',methods=['POST','GET'])
def changeseller():
    if request.method=='POST':
        seller=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update sellervset name=? where id=?',(name))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removeseller',methods=['POST','GET'])
def removeseller():
    seller=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from seller where id=?',(name))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')

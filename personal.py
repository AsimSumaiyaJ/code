import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('personal.html')
@app.route('/createpersonal')
def createpersonal():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table personal(id int not null,name char(17),dateofbirth char(10),gender char(1),phonenumber char(10),emailaddress char(31),address char(80))')
        cn.close()
        return jsonify('')
@app.route('/addpersonal/',methods=['POST','GET'])
def addpersonal():
    #if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=opersonal['name']
        dateofbirth=opersonal['dateofbirth']
        gender=opersonal['gender']
        phonenumber=opersonal['phonenumber']
        emailaddress=opersonal['emailaddress']
        address=opersonal['address']
        cn.execute('insert into personal(name,dateofbirth,gender,phonenumber,emailaddress,address)values(?,?,?,?,?,?)',(name,dateofbirth,gender,phonenumber,emailaddress,address))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/')
def getpersonal():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,dateofbirth,gender,phonenumber,emailaddress,address from personal')
        lpersonal=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getpersonalcount',methods=['GET','POST'])
def getpersonalcount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from personal')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getpersonalid')
def getpersonalid():
    if request.method=='GET':
        id=request.get_json()
        cn= cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,dateofbirth,gender,phonenumber,emailaddress,address from personal where id=?',id)
        opersonal=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changepersonal',methods=['POST','GET'])
def changepersonal():
    if request.method=='POST':
        personal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update personal set name=?,dateofbirth=?,gender=?,phonenumber=?,emailaddress=?,address=? where id=?',(name,dateofbirth,gender,phonenumber,emailaddress,address))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removepersonal',methods=['POST','GET'])
def removepersonal():
    personal=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from personal where id=?',(name,dateofbirth,gender,phonenumber,emailaddress,address))
    cn.commit()
    cn.close()
    return jsonify('') 
if __name__=='__main__':
  app.run=('True')

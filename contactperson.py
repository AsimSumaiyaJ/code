import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('flash')
def index():
    return render_template('contactperson.html')
@app.route('/createcontactperson')
def createcontactperson():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table contactperso(name char(17),phonenumber char(10),emailaddress char(31))')
        cn.close()
        return jsonify('')
@app.route('/addcontactperson/.methods=['POST','GET']')
def addcontactperson():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=opersonal['name']
        phonenumber=opersonal['phonenumber']
        emailaddress=opersonal['emailaddress']
        cn.execute('insert into contactperson(name,phonenumber,emailaddress)values(?,?,?)',(name,phonenumber,emailaddress))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('')
def getcontactperson():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,phonenumber,emailaddress from contactperson')
        lpersonal=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getcontactpersoncount',methods=['GET','POST'])
def getcontactpersoncount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from contactperson')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getcontactpersonid')
def getcontactpersonid():
    if request.method=='GET':
        id=request.get_json()
        cn= cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,phonenumber,emailaddress from contactperson where id=?',id)
        opersonal=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changecontactperson',methods=['POST','GET'])
def changecontactperson():
    if request.method=='POST':
        personal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update contactperson set name=?,phonenumber=?,emailaddress=? where id=?',(name,phonenumber,emailaddress))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removecontactperson',methods=['POST','GET'])
def removecontactperson():
    contactperson=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from contactperson where id=?',(name,phonenumber,emailaddress))
    cn.commit()
    cn.close()
    return jsonify('')
if __name__=='__main__':
app.run=('True')

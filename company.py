import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('company.html')
@app.route('/createcompany')
def createcompany():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table company(name char(17),address char(80),website char(22))')
        cn.close()
        return jsonify('')
@app.route('/addcompany/',methods=['POST','GET'])
def addcompany():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=opersonal['name']
        address=opersonal['address']
        website=opersonal['website']
        cn.execute('insert into company(name,address,website)values(?,?,?)',(name,address,website))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getcompany')
def getcompany():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,address,website from company')
        lpersonal=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getcompanycount',methods=['GET','POST'])
def getcompanycount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from company')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getcompanyid')
def getcompanyid():
    if request.method=='GET':
        id=request.get_json()
        cn= cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,address,website from company where id=?')
        opersonal=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changecompany',methods=['POST','GET'])
def changecompany():
    if request.method=='POST':
        personal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update company set name=?,address=?,website=? where id=?',(name,address,website))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removecompany',methods=['POST','GET'])
def removecompany():
    company=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from company where id=?',(name,address,website))
    cn.commit()
    cn.close()
    return jsonify('')
if __name__=='__main__':
    app.run(debug=True)

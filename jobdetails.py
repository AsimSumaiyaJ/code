import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('jobdetails.html')
@app.route('/createjobdetails')
def createjobdetails():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table jobdetails( company char(24),qualification char(8),technologies char(40),experience int)')
        cn.close()
        return jsonify('')
@app.route('/addjobdetails/',methods=['POST','GET'])
def addjobdetails():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        company=opersonal['company']
        qualification=opersonal['qualification']
        technologies=opersonal['technologies']
        experience=opersonal['experience']
        cn.execute('insert into jobdetails(company,qualification,technologies,experience)values(?,?,?,?)',(company,qualification,technologies,experience))
        cn.close()
        return jsonify('')
@app.route('/getjobdetails')
def getjobdetails():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select company,qualification,technologies,experience from jobdetails')
        lpersonal=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getjobdetailscount',methods=['GET','POST'])
def getjobdetailscount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from jobdetails')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
app.route('/getjobdetailsid')
def getjobdetailsid():
    if request.method=='GET':
        id=request.get_json()
        cn= cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select company,qualification,technologies,experience from jobdetails where id=?')
        opersonal=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changejobdetails',methods=['POST','GET'])
def changejobdetails():
    if request.method=='POST':
        jobdetails=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update jobdetails set company=?,qualification=?,technologies=?,experience=? where id=?',(company,qualification,technologies,experience))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removejobdetails',methods=['POST','GET'])
def removejobdetails():
    jobdetails=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from jobdetails where id=?',(company,qualification,technologies,experience))
    cn.commit()
    cn.close()
    return jsonify('')
if __name__=='__main__':
    app.run(debug=True)

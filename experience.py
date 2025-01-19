import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('experience.html')
@app.route('/createexperience')
def createexperience():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table experience(company char(24),technologies char(40),startdate char(10),enddate char(10))')
        cn.close()
        return jsonify('')
@app.route('/addexperience/',methods=['POST','GET'])
def addexperience():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        company=opersonal['company']
        technologies=opersonal['technologies']
        startdate=opersonal['startdate']
        enddate=opersonal['enddate']
        cn.execute('insert into experience(company,tecnologies,startdate,enddate)values(?,?,?,?)',(company,tecnologies,startdate,enddate))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getexperience')
def getexperience():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select company,tecnologies,startdate,enddate from experience')
        lpersonal=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getexperiencecount',methods=['GET','POST'])
def getexperiencecount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from experience')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getexperienceid')
def getexperienceid():
    if request.method=='GET':
        id=request.get_json()
        cn= cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select company,tecnologies,startdate,enddate from experience' where id=?)
        opersonal=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changeexperience',methods=['POST','GET'])
def changeexperience():
    if request.method=='POST':
        experience=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update experience set company=?,technologies=?,startdate=?,enddate=? where id=?',(company,technologies,startdate,enddate))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removeexperience',methods=['POST','GET'])
def removeexperience():
    experience=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from experience where id=?',(company,technologies,startdate,enddate))
    cn.commit()
    cn.close()
    return jsonify('')
if __name__=='__main__':
     app.run=('True')

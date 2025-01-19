import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('education.html')
@app.route('/createducation')
def createeducation():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table education(course char(8),school/college char(6),board/university char(17),startdate char(10),enddate char(10),marks int,completed char(1))')
        cn.close()
        return jsonify('')
@app.route('/addpersonal/',methods=['POST','GET'])
def addeducation():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        course=opersonal['course']
        schoolcollege=opersonal['schoolcollege']
        boarduniversity=opersonal['boarduniversity']
        startdate=opersonal['startdate']
        enddate=opersonal['enddate']
        marks=opersonal['marks']
        completed=opersonal['completed']
        cn.execute('insert into education(course,schoolcollege,boarduniversity,startdate,enddate,marks,completed)values(%s,%s,%s,%s,%s,%s,%s)',(course,schoolcollege,boarduniversity,startdate,enddate,marks,completed))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/geteducation')
def geteducation():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select course,schoolcollege,boarduniversity,startdate,enddate,marks,completed from education')
        lpersonal=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/geteducationcount',methods=['GET','POST'])
def geteducationcount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from education')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/geteducationid')
def geteducationid():
    if request.method=='GET':
        id=request.get_json()
        cn= cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select course,schoolcollege,boarduniversity,startdate,enddate,marks,completed from education' where id=?)
        opersonal=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changeeducation',methods=['POST','GET'])
def changeeducation():
    if request.method=='POST':
        education=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update education set course=?,school/college=?,board/university=?,startdate=?,enddate=?,marks=?,completed=? ',(course,school/college,board/university,startdate,enddate,marks,completed))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removeeducation',methods=['POST','GET'])
def removeeducation():
    education=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from education where id=?',(course,school/college,board/university,startdate,enddate,marks,completed))
    cn.commit()
    cn.close()
    return jsonify('')
if __name__=='__main__':
    app.run(debug=True)

import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('candidateselected.html')
@app.route('/createcandidateselected')
def createcandidateselected():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table candidateselected(commission int)')
        cn.close()
        return jsonify('')
@app.route('/addcandidateselected/',methods=['POST','GET'])
def addcandidateselected():
    if request.method=='POST':
        opersonal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        commission=opersonal['commission']
        cn.execute('insert into candidateselected(commission)values(?)'),(commission)
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getcandidateselected')
def getcandidateselected():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select commission from candidateselected')
        lpersonal=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getcandidateselectedcount',methods=['GET','POST'])
def getcandidateselectedcount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from candidateselected')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getcandidateselectedid')
def getcandidateselectedlid():
    if request.method=='GET':
        id=request.get_json()
        cn= cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select commission from candidateselected where id=?',id)
        opersonal=cu.fetchall()
        cn.close()
        return jsonify('opersonal')
@app.route('/changecandidateselected',methods=['POST','GET'])
def changecandidateselected():
    if request.method=='POST':
        personal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update candidateselected set commission=? where id=?',(commission))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removecandidateselected',methods=['POST','GET'])
def removecandidateselected():
    personal=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from candidateselected where id=?',(commission))
    cn.commit()
    cn.close()
    return jsonify('')
if __name__=='__main__':
   app.run(debug=True)

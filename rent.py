import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('rent.html')
@app.route('/createrent')
def createrent():
    if request.method=='POST':
        omovie=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table rent(moviename char(17),copy int,customerid int,rentdatetime char(10),returndatetime char(10))')
        cn.close()
        return jsonify('')
@app.route('/addrent/',methods=['POST','GET'])
def addrent():
    if request.method=='POST':
        orent=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=orent['name']
        copy=orent['copy']
        cn.execute('insert into rent(moviename,copy,customerid,rentdatetime,returndatetime)values(?,?,?,?,?)',(moviename,copy,customerid,rentdatetime,returndatetime))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getrent')
def getrent():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select moviename,copy,customerid,rentdatetime,returndatetime from rent')
        lrent=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getrentcount',methods=['GET','POST'])
def getrentcount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from rent')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getrentid')
def getrentid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select  moviename,copy,customerid,rentdatetime,returndatetime from rent where id=?',id)
        orent=cu.fetchall()
        cn.close()
        return jsonify('orent')
@app.route('/changerent',methods=['POST','GET'])
def changerent():
    if request.method=='POST':
        rent=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update rent set moviename=?,copy=?,customerid=?,rentdatetime=?,returndatetime=? where id=?',(moviename,copy,customerid,rentdatetime,returndatetime))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removerent',methods=['POST','GET'])
def removerent():
    rent=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from rent where id=?',(moviename,copy,customerid,rentdatetime,returndatetimey))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')

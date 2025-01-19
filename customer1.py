import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('customer1.html')
@app.route('/createcustomer1')
def createcustomer1():
    if request.method=='POST':
        ocustomer1=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table customer1(name char(17),phonenumber int,address char(30))')
        cn.close()
        return jsonify('')
@app.route('/addcustomer1/',methods=['POST','GET'])
def addcustomer1():
    if request.method=='POST':
        ocustomer1=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=ocustomer1['customername ']
        phonenumber=ocustomer1['phonenumber']
        address=ocustomer1['address']
        cn.execute('insert into customer1( name,phonenumber,address)values(?,?,?)',(customername,phonenumber,address))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getcustomer1')
def getcustomer1():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,phonenumber,address from customer1')
        lcustomer1=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getcustomer1count',methods=['GET','POST'])
def getcustomer1count():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from customer1')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getcustomerid')
def getcustomerid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select name,phonenumber,address from customer where id=?',id)
        ocustomer=cu.fetchall()
        cn.close()
        return jsonify('ocustomer')
@app.route('/changecustomer1',methods=['POST','GET'])
def changecustomer1():
    if request.method=='POST':
        customer1=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update customer set name=?,phonenumber=?,address=? where id=?',(name,phonenumber,address))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removecustomer1',methods=['POST','GET'])
def removecustomer1():
    customer1=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from customer1 where id=?',(name,phonenumber,address))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')
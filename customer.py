import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('customer.html')
@app.route('/createcustomer')
def createcustomer():
    if request.method=='POST':
        ocustomer=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table customer(customername char(17),depositamt int)')
        cn.close()
        return jsonify('')
@app.route('/addcustomer/',methods=['POST','GET'])
def addcustomer():
    if request.method=='POST':
        ocustomer=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        name=ocustomer['customername ']
        copy=ocustomer['depositamt']
        cn.execute('insert into customer(customername,depositamt)values(?,?)',(customername,depositamt))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getcustomer')
def getcustomer():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select customername,depositamt from customer')
        lcustomer=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getcustomercount',methods=['GET','POST'])
def getcustomercount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from customer')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getcustomerid')
def getcustomerid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select customername,depositamt from customer where id=?',id)
        ocustomer=cu.fetchall()
        cn.close()
        return jsonify('ocustomer')
@app.route('/changecustomer',methods=['POST','GET'])
def changecustomer():
    if request.method=='POST':
        personal=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update customer set name=?,copy=? where id=?',(customername,depositamt))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removecustomer',methods=['POST','GET'])
def removecustomer():
    customer=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from customer where id=?',(customername,depositamt))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')

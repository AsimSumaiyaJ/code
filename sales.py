import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('sales.html')
@app.route('/createsales')
def createsales():
    if request.method=='POST':
        osales=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table sales( productid int,quantity int,customerid int)')
        cn.close()
        return jsonify('')
@app.route('/addsales/',methods=['POST','GET'])
def addsales():
    if request.method=='POST':
        osales=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        productid=osales['productid']
        quantity=osales['quantity']
        sellerid=osales['sellerid']
        cn.execute('insert into sales(productid,quantity,customerid)values(?,?,?)',(productid,quantity,customerid))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getsales')
def getsales():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select productid,quantity,customerid from sales')
        lsales=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getsalescount',methods=['GET','POST'])
def getsalescount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from sales')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getsalesid')
def getsalesid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select productid,quantity,customerid from sales where id=?',id)
        osales=cu.fetchall()
        cn.close()
        return jsonify('osales')
@app.route('/changesales',methods=['POST','GET'])
def changesales():
    if request.method=='POST':
        sales=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update sales set productid=?,quantity=?,customerid=? where id=?',(productid,quantity,customerid))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removesales',methods=['POST','GET'])
def removesales():
    sales=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from sales where id=?',(productid,quantity,customerid))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')

import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('purchase.html')
@app.route('/createpurchase')
def createpurchase():
    if request.method=='POST':
        opurchase=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table purchase(productid int,quantity int,sellerid int)')
        cn.close()
        return jsonify('')
@app.route('/addpurchase/',methods=['POST','GET'])
def addpurchase():
    if request.method=='POST':
        opurchase=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        productid=opurchase['productid']
        quantity=opurchase['quantity']
        sellerid=opurchase['sellerid']
        cn.execute('insert into purchase(productid,quantity,sellerid)values(?,?,?)',(productid,quantity,sellerid))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getpurchase')
def getpurchase():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select productid,quantity,sellerid from purchase')
        lpurchase=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getpurchasecount',methods=['GET','POST'])
def getpurchasecount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from purchase')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getpurchaseid')
def getpurchaseid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select productid,quantity,sellerid from purchase where id=?',id)
        opurchase=cu.fetchall()
        cn.close()
        return jsonify('omovie')
@app.route('/changepurchase',methods=['POST','GET'])
def changepurchase():
    if request.method=='POST':
        purchase=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update purchase set productid=?,quantity=?,sellerid=? where id=?',(productid,quantity,sellerid))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removepurchase',methods=['POST','GET'])
def removepurchase():
    purchase=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from purchase where id=?',(productid,quantity,sellerid))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')

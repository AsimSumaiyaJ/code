import json 
import sqlite3
from flask import Flask,render_template, request, url_for,jsonify
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('product.html')
@app.route('/createproduct')
def createproduct():
    if request.method=='POST':
        oproduct=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('create table product(productid int,productname char(17),costprice int,sellingprice int,buyingdatetime date,sellingdatetime date)')
        cn.close()
        return jsonify('')
@app.route('/addproduct/',methods=['POST','GET'])
def addproduct():
    if request.method=='POST':
        oproduct=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        productid=oproduct['productid']
        productname=oproduct['productname']
        costprice=oproduct['costprice']
        sellingprice=oproduct['sellingprice']
        buyingdatetime=oproduct['buyingdatetime']
        sellingdatetime=oproduct['sellingdatetime']
        cn.execute('insert into product(productid,productname,costprice,sellingprice,buyingdatetime,sellingdatetime)values(?,?,?,?,?,?)',(productid,productname,costprice,sellingprice,buyingdatetime,sellingdatetime))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/getproduct')
def getproduct():
    if request.method=='GET':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select productid,productname,costprice,sellingprice,buyingdatetime,sellingdatetime from product')
        lmovie=cu.fetchall()
        cn.close()
        return jsonify('')
@app.route('/getproductcount',methods=['GET','POST'])
def getproductcount():
    if request.method=='POST':
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select count(*) from product')
        cu=cu.fetchall()
        cn.close
        return jsonify('')
@app.route('/getproductid')
def getproductid():
    if request.method=='GET':
        id=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('select productid,productname,costprice,sellingprice,buyingdatetime,sellingdatetime from product where id=?',id)
        oproduct=cu.fetchall()
        cn.close()
        return jsonify('oproduct')
@app.route('/changeproduct',methods=['POST','GET'])
def changeproduct():
    if request.method=='POST':
        product=request.get_json()
        cn=sqlite3.connect('test.db')
        cu=cn.cursor
        cn.execute('update product set productid=?,productname=?,costprice=?,sellingprice=?,buyingdatetime=?,sellingdatetime=? where id=?',(productid,productname,costprice,sellingprice,buyingdatetime,sellingdatetime))
        cn.commit()
        cn.close()
        return jsonify('')
@app.route('/removeproduct',methods=['POST','GET'])
def removeproduct():
    product=request.get_json()
    cn=sqlite3.connect('test.db')
    cu=cn.cursor
    cn.execute('delete from product where id=?',(productid,productname,costprice,sellingprice,buyingdatetime,sellingdatetime))
    cn.commit()
    cn.close()
    return jsonify('')  
if __name__=='__main__':
  app.run=('True')

from flask import Flask,request,session,redirect,url_for,Blueprint
from flask import abort,render_template,flash
data=Blueprint('data',__name__)
@data.route('/')
@data.route('/<type>/<name>')
def data(type=None,name=None):
	data1=['apple','pea','banana']
	data2=['z','f','x']
	if type=='bug':
		return render_template('showdata.html',name=name,data=data1)
	elif type=='code':
		return render_template('showdata.html',name=name,data=data2)
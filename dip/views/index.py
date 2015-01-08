from dip import app
from flask import Flask,url_for,render_template,g,current_app,request,abort,redirect,flash,session,escape
from paginate import Pagination
from pymongodb import mongoDB
import os.path
import sys
import logging
from logging import FileHandler
from werkzeug.datastructures import ImmutableMultiDict
from dip import user_db
from dip import db
@app.route('/')
def index():
    
    error=None
    if session.has_key('logged_in'):
        return render_template('index.html',error=error)
    else:
        return render_template('login.html',error=error)

@app.route('/login',methods=['GET','POST'])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
def login():
    error=None
    data={}
    if request.method == 'POST':
        data['name']=request.form['name']
        data['password']=request.form['password'] 

    app.logger.error(str(data))
    flag = user_db.authenticate(data)
    app.logger.error(str(flag))
    if flag:
            #return redirect(url_for('index'))
        
        session['logged_in'] = True
        session['username'] = request.form['name']

        return redirect(url_for('index'))
      #return redirect(url_for('show_log'))
    return render_template('login.html',error=error)

@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    data={}
    if request.method == 'POST':
    	data['name']=request.form['name']
        data['mail']=request.form['mail']
        data['password']=request.form['password']
    return data['name']
    user_db.add(data)
    app.logger.error(data['name'])
    app.logger.error(str(data))
    return data['password']

@app.route('/logout')
def logout():
    error=None
    session.pop('logged_in',None)
    return render_template('login.html',error=error)


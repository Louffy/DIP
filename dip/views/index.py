from dip import app
from flask import Flask,url_for,render_template,g,current_app,request,abort,redirect,flash,session,escape
from paginate import Pagination
from pymongodb import mongoDB
import os.path
import sys
import logging
from logging import FileHandler
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
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            #return redirect(url_for('index'))
            session['logged_in'] = True
            session['username'] = request.form['username']
            return redirect(url_for('index'))
      #return redirect(url_for('show_log'))
    return render_template('login.html',error=error)

@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
    	data=request.form
    #user_db.add(data)
    logging
    return data

@app.route('/logout')
def logout():
    error=None
    session.pop('logged_in',None)
    return render_template('login.html',error=error)


#-*- coding: utf-8 -*-
from dip import app
from flask import Flask,url_for,render_template,g,current_app,request,abort,redirect,flash,session,escape
from paginate import Pagination
from pymongodb import mongoDB
import os.path
import sys
import logging
from logging import FileHandler

from dip import db
data_schama={
    'git':['vcs','repo','n_dev','n_cmt','begin_t','end_t','loc']
}

@app.route('/user/<username>',methods=['GET'])
def show_user_profile(username):
    zfx=request.args.get('zfx')
    return 'User is %s' % zfx

@app.route('/data/list',methods=['GET'])
def data_list():
    #console.log("data start")
    #name=request.args.get('type')
    name=request.args.get('type')
    c_data=[]
    #return render_template('showdata.html',entries=entries)
    search = False
    q = request.args.get('q')
    if q:
        search = True
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1
    per_page=10
    logging.info(name)
    if search == True:
       # console.log("search==True")
        data=db.findQuery(name,q)
    else:
        data = db.findAll(name)

    index=(page-1)*per_page
    delta=per_page
    if (len(data)-index)/per_page == 0:
        delta=len(data)-index

  

    for i in range( index, index+delta):
        c_data.append(data[i])
    if search == True:
      pagination = Pagination(page=page, total=len(data), search=search, record_name='Id',found=len(data),search_msg=q,)
    else:
      pagination = Pagination(page=page, total=len(data), search=search, record_name='Id',)

    keys=[]
    if len(c_data) > 0:
      keys=c_data[0].keys()
    return render_template('list.html',
                           c_data=c_data,
                           keys=keys,
                           page=page,
                           per_page=per_page,
                           total=len(data),
                           pagination=pagination,
                           name=name,
                           )


@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

#@app.route('/login',methods=['GET','POST'])
#def login():
#	if request.method == 'POST':
#		do_the_login()
#	else:
#		show_the_login_form()

@app.route('/data')
def showdata():
	types=data_types
	return render_template('data.html')

@app.route('/data/add_data')
def add_data():
    name=request.args.get('type')
    table=data_schama[name]
    #return table[2]
    return render_template('add.html',type=name,data=table)
@app.route('/data/onedata',methods=['GET'])
def show_data():
    name=request.args.get('type')
    repo=request.args.get('repo')
    data=db.findOneByName(str(name),'repo',str(repo))
    return render_template('onedata.html',type=name,data=data_schama[name],onedata=data)

@app.route('/data/edit',methods=['GET','POST'])
def edit_data():
    name=request.args.get('type')
    repo=request.args.get('repo')
    data=db.findOneByName(str(name),'repo',str(repo))
    return render_template('edit.html',type=name,data=data_schama[name],onedata=data)

@app.route('/data/delete')
def delete_data():
    return "dddddd"

@app.route('/data/update',methods=['GET','POST'])
def update_data():
    return "dddddd"

@app.route('/data/code_log',methods=['GET'])
def show_log():
    #console.log("data start")
    #name=request.args.get('type')
    name=request.args.get('type')
    c_data=[]
    #return render_template('showdata.html',entries=entries)
    search = False
    q = request.args.get('q')
    if q:
		search = True
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1
    per_page=10

    if search == True:
       # console.log("search==True")
        data=db.findQuery(name,q)
    else:
        data = db.findAll(name)

    index=(page-1)*per_page
    delta=per_page
    if (len(data)-index)/per_page == 0:
        delta=len(data)-index

	

    for i in range( index, index+delta):
        c_data.append(data[i])
    if search == True:
	    pagination = Pagination(page=page, total=len(data), search=search, record_name='repo',found=len(data),search_msg=q,)
    else:
	    pagination = Pagination(page=page, total=len(data), search=search, record_name='repo',)
    return render_template('data.html',
                           c_data=c_data,
                           page=page,
                           per_page=per_page,
                           total=len(data),
                           pagination=pagination,
                           name=name,
                           )

@app.route('/data/script',methods=['GET'])
def show_script():
    name='script'
    c_data=[]
    #return render_template('showdata.html',entries=entries)
    search = False
    q = request.args.get('q')
    if q:
        search = True
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1
    per_page=10

    if search == True:
       # console.log("search==True")
        data=db.findQuery(name,q)
    else:
        data = db.findAll(name)

    index=(page-1)*per_page
    delta=per_page
    if (len(data)-index)/per_page == 0:
        delta=len(data)-index

  

    for i in range( index, index+delta):
        c_data.append(data[i])
    if search == True:
        pagination = Pagination(page=page, total=len(data), search=search, record_name='script',found=len(data),search_msg=q,)
    else:
        pagination = Pagination(page=page, total=len(data), search=search, record_name='script',)
    return render_template('script_data.html',
                           c_data=c_data,
                           page=page,
                           per_page=per_page,
                           total=len(data),
                           pagination=pagination,
                           name=name,
                           )
#'''
#@app.route('/data/script/<name>')
#def show_script_name(name):
 #   data=db.findOneByName('script','script_name',name)
  #  return data['loc']
    #return 'user is %s' % name
#''' 


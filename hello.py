#-*- coding: utf-8 -*-
import os
os.environ['PYTHON_EGG_CACHE']= '/var/pkuas/tmp'
from flask import Flask,url_for,render_template,g,current_app,request,abort,redirect,flash,session,escape
from paginate import Pagination
from pymongodb import mongoDB
import os.path
import sys
import logging
from logging import FileHandler

reload(sys)
app = Flask(__name__)

app.config['USERNAME']='pkuas'
app.config['PASSWORD']='pkuas'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

db = mongoDB('datashare')

data_types=['code_log']
log_types=['log']

file_handler=FileHandler("/var/pkuas/debug.log","a")
#file_handler=FileHandler("/var/www/hello/debug.log","a")
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)


data_schama={
    'git':['vcs','repo','n_dev','n_cmt','begin_t','end_t','loc']
}


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
    return "test"

@app.route('/logout')
def logout():
    error=None
    session.pop('logged_in',None)
    return render_template('login.html',error=error)


@app.route('/')
def index():
    
    error=None
    if session.has_key('logged_in'):
        return render_template('index.html',error=error)
    else:
        return render_template('login.html',error=error)

@app.route('/user/<username>',methods=['GET'])
def show_user_profile(username):
    zfx=request.args.get('zfx')
    return 'User is %s' % zfx

@app.route('/user/list',methods=['GET'])
def list():
	search = False
	q = request.args.get('q')
	if q:
		search = True
	try:
		page = int(request.args.get('page', 1))
	except ValueError:
		page = 1

	users = ['a','a','a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','b','b','b','b','b','b','b','b']
	print users
	pagination = Pagination(page=page, total=len(users), search=search, record_name='users',)
	return render_template('hello.html',
                           users=users,
                           page=page,
                           pagination=pagination,
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


if __name__=='__main__':
	
	  app.run()

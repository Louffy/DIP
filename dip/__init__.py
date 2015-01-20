import os
os.environ['PYTHON_EGG_CACHE']= '/var/pkuas/tmp'
from flask import Flask,url_for,render_template,g,current_app,request,abort,redirect,flash,session,escape
from paginate import Pagination
from pymongodb import mongoDB
import os.path
import sys
import logging
from logging import FileHandler


app=Flask(__name__)
db = mongoDB('datashare')

from dip.models.user_m import Userquery
user_db=Userquery()

import dip.views.user
import dip.views.index
import dip.views.data

reload(sys)

app.config['USERNAME']='pkuas'
app.config['PASSWORD']='pkuas'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



data_types=['code_log']
log_types=['log']

file_handler=FileHandler("./debug.log","a")
#file_handler=FileHandler("/var/www/hello/debug.log","a")
file_handler.setLevel(logging.NOTSET)
app.logger.addHandler(file_handler)
app.logger.error("Debug BEGIN!!!!!!!\n")


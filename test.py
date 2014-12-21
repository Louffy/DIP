#auther:Feixue Zhang
#usage: ./**.py
import os,sys
from pymongodb import mongoDB

header=['script_name','loc','purpose','input','output','usage']
db=mongoDB('datashare')


all=db.findOneByName('script','script_name','dosfnew.perl')
print all

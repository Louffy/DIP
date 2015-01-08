import pymongo
import hashlib
import os
from dip import db



class Userquery:
	
	user=db.db['user']

	def authenticate(self,data):
		u1=self.user.find_one({'name':data['name'],'password':data['password']})
		if u1:
			return True
		else:
			return False
		

	def add(self,data):
		id=self.user.insert(data)
		return id
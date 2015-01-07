import pymongo
import hashlib
from dip import db



class Userquery:
	
	user=db.db['user']

	def authenticate(self,data):
		return self.user.find_one(data)

	def add(self,data):
		id=self.user.insert(data)
		return id
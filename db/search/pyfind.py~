#!/usr/bin/python

import sys
sys.path.append('..')
from service.mongoDB import mongoDB

class find(object):
    
    def __init__(self):
        self.db = mongoDB('datashare').get_db()
        
    def __EQ__(self, collection, key, val):
        posts = self.db[str(collection)].find({key : val})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __NE__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$ne' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __LT__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$lt' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __GT__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$gt' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __LTE__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$lte' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __GTE__(self, collection, key, val):
        posts = self.db[str(collection)].find({str(key) : {'$gte' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    
    def __IN__(self, collection, key, *val):
        posts = self.db[str(collection)].find({str(key) : {'$in' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __NIN__(self, collection, key, *val):
        posts = self.db[str(collection)].find({str(key) : {'$nin' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        
    def __ALL__(self, collection, key, *val):
        posts = self.db[str(collection)].find({str(key) : {'$all' : val}})
        ret = []
        for post in posts:
            ret.append(post)
        return ret
    
    def __AND__(self, collection, arg):
        posts = self.db[str(collection)].find(arg)
        ret = []
        for post in posts:
            ret.append(post)
        return ret
        

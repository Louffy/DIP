#!/usr/bin/python
#usage ./insert_script "file_name"                                                                

import sys
sys.path.append('..')
from service.mongoDB import mongoDB

header=['name','loc','cata','in','out','des']
db = mongoDB('datashare')

def readData():
    try:
        in_file = open(sys.argv[1])
        ret = []
        for line in in_file:
            item = {}
            line = line.strip('\n')
            sp = line.split(';')
            for i in range(0, len(sp)):
                item[header[i]] = sp[i]
            ret.append(item)
        return ret
    except:
        usage.__call__()

def insertDB(data):
    collection = 'script'
    for i in range(0, len(data)):
        db.insert(collection, data[i])

def usage():
    print 'usage: ./insert_script "file_name" '

data = readData()
insertDB(data)

#!/usr/bin/python
#usage ./insert_script "file_name" "maillist"                                                    

import sys
from mongoDB import mongoDB

header=['mlist','repo','proj','n_mail','n_peo','loc']
dict_mlist={'mbox':'mbox_info', 'mailman':'mailman_info'}
db = mongoDB('datashare')

def readData():
    in_file = open(sys.argv[1])
    ret = []
    for line in in_file:
        item = {}
        line = line.strip('\n')
        sp = line.split(';')
        sp[3] = int(sp[3])
        sp[4] = int(sp[4])
        for i in range(0, len(sp)):
            item[header[i]] = sp[i]
        ret.append(item)
    return ret

def insertDB(mlist, data):
    if mlist not in dict_mlist.keys():
        usage.__call__()
    else:
        collection = dict_mlist[mlist]
        for i in range(0, len(data)):
            db.insert(collection, data[i])

def usage():
    print "usage:"
    print sys.argv[2] + ' mbox|mailman'

data = readData()
insertDB(sys.argv[2],data)

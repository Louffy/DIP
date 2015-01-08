#!/usr/bin/python
#usage ./insert_log  "file_name" "vcs"                                                       

import sys
sys.path.append('..')
from service.mongoDB import mongoDB

header=['vcs','repo','prj','n_peo','n_cmt','b_time','e_time','span','log_loc','src_loc']
dict_vcs={'svn':'svn_info', 'git':'git_info', 'hg':'hg_info', 'bazaar':'baz_info'}
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
        sp[5] = int(sp[5])
        sp[6] = int(sp[6])
        sp[7] = int(sp[7])
        for i in range(0, len(sp)):
            item[header[i]] = sp[i]
        ret.append(item)
    return ret

def insertDB(vcs, data):
    if vcs not in dict_vcs.keys():
        usage.__call__()
    else:
        collection = dict_vcs[vcs]
        for i in range(0, len(data)):
            db.insert(collection, data[i])

def usage():
    print "usage:"
    print sys.argv[2] + ' svn|git|hg|bazaar'

data = readData()
insertDB(sys.argv[2], data)

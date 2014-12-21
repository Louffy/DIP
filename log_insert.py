import os,sys
from pymongodb import mongoDB

header=['vcs','repo','n_dev','n_cmt','begin_t','end_t','loc']
db=mongoDB('datashare')

def readData():
	f = file(sys.argv[1])
#	print sys.argv[1]

	allData=[]

	while True:
		item={}
		line=f.readline()

		if len(line) == 0:
			break

#		print line
		terms=line.split(';')
		
		for i in range(0,len(terms)):
			item[header[i]]=terms[i]

#		print item

		allData.append(item)


#	print allData
	return allData

def insertDB(collection,alldata):

	
	for i in range(0,len(alldata)):
		db.insert(collection,alldata[i])

	#data={'name':'zfx','age':'24'}
	#print db.insert('log',data)
	#print db.findOne('log',{'name':'zfx'})
file_d=readData()
insertDB(sys.argv[2],file_d)
all=db.findAll(sys.argv[2])
print all

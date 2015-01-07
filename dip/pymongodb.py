import pymongo

class mongoDB:

	def __init__(self,db):
		client=pymongo.MongoClient('127.0.0.1', 27017)
		self.db=client[db]
			

	def insert(self,collection,document):
		collection=self.db[collection]
		id=collection.insert(document)
		return id
	
	def findOneByName(self,collection,name1,name2):
		return self.db[collection].find_one({name1:name2})

	def findAll(self,collection):
		posts = self.db[collection].find()
		posts.sort('repo',pymongo.ASCENDING)
		allData = []
		for post in posts:
			#print(post)
			allData.append(post)

		return allData

	def findQuery(self,collection,query):
        	posts = self.db[str(collection)].find({"loc":{"$regex":str(query)}})
        	posts.sort('repo',pymongo.ASCENDING)
        	allData = []
        	for post in posts:
			#print(post)
			allData.append(post)

        	return allData


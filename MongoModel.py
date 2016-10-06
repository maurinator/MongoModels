class Model:

	def __init__(self, db, tName):
		self.db = db
		self.tName = tName

	def createModel(self) :
		if self.tName in self.db.collection_names():
			print ("model already exists")
		else:
			print("Model " + self.tName + " created.")
			self.db.create_collection(self.tName)

	def deleteModel(self):
		if self.tName in self.db.collection_names():
			print("Model " + self.tName + " deleted.")
			self.db[self.tName].drop()
		else:
			print ("model does not exist")

	def printModel(self):
		if self.tName in self.db.collection_names():
			for item in self.db[self.tName].find():
				print item
		else:
			print ("model does not exist")
			
	def insertIntoModel(self, items):
		if self.tName in self.db.collection_names():
			for item in items:
				row_id = self.db[self.tName].count()
				item['row_id'] = row_id
				print("Add '" + str(item) + "' to model '" + self.tName + "'.")
				self.db[self.tName].insert(item)
		else:
			print ("model does not exist")

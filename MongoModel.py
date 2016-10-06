class Model:

	def __init__(self, db, tName):
		self.db = db
		self.tName = tName
		self.exists = self.tName in self.db.collection_names()

	def createModel(self) :
		if self.exists:
			print ("model already exists")
		else:
			print("Model " + self.tName + " created.")
			self.db.create_collection(self.tName)
			self.exists = True

	def deleteModel(self):
		if self.exists:
			print("Model " + self.tName + " deleted.")
			self.db[self.tName].drop()
			self.exists = False
		else:
			print ("model does not exist")

	def printModel(self):
		if self.exists:
			for item in self.db[self.tName].find():
				print item
		else:
			print ("model does not exist")

	def insertIntoModel(self, items):
		if exists:
			for item in items:
				row_id = self.db[self.tName].count()
				item['row_id'] = row_id
				print("Add '" + str(item) + "' to model '" + self.tName + "'.")
				self.db[self.tName].insert(item)
		else:
			print ("model does not exist")

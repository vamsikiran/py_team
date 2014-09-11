from pymongo import Connection
databaseName = "test"
connection = Connection()
db = connection['databaseName']
employees = db['employees']

person1 = {'name': 'John Doe'}

employees.save(person1)
for e in employees.find():
	print e['name']
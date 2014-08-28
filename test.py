from framework.weberdb import WeberDB

w = WeberDB()
print w.collection_names()

print w.find_document('user', 'name','ratanraj')


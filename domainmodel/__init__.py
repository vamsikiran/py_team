from weber.settings import weber_db

class Model(object):
    collection_name = None
    def __init__(self, *args, **kwargs):
        pass
    def save(self):
        pass
    def encode(self):
        pass
    def decode(self):
        pass

    @classmethod
    def getByFieldValue(cls, field, value):
        attrs = weber_db.find_document(cls.collection_name, field, value)
        if attrs:
            return cls(attrs)
        else:
            None



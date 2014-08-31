from weber.settings import weber_db

class Model(object):
    collection_name = None
    def __init__(self, *args, **kwargs):
        self.attrs = kwargs.get('attrs',{})
        
    def save(self):
        pass
    def encode(self):
        pass
    def decode(self):
        pass

    def __getattr__(self,attr_name):
        try:
            return self.attrs['object'][attr_name]
        except:
            raise AttributeError

    @classmethod
    def getByFieldValue(cls, field, value):
        attrs = weber_db.find_document(cls.collection_name, field, value)
        if attrs:
            return cls(attrs=attrs)
        else:
            None



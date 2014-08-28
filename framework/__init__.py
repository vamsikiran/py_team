"""
The Framework module
"""
from django.http.response import HttpResponseNotFound, HttpResponseBadRequest,\
    Http404
from weber.settings import weber_db

class WeberView(object):
    def __init__(self, request):
        self.request=request

    def get(self, *args, **kwargs):
        raise Http404

    def post(self, *args, **kwargs):
        return Http404

    @classmethod
    def as_view(cls, request, *args, **kwargs):
        if request.method=='GET':
            return cls(request).get(*args, **kwargs)
        elif request.method=='POST':
            return cls(request).get(*args, **kwargs)
        else:
            return HttpResponseBadRequest("Invalid Request")


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

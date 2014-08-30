"""
The Framework module
"""
from django.http.response import HttpResponseNotFound, HttpResponseBadRequest,\
    Http404

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



from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from framework import WeberView
import json
from django.http.response import Http404


class Service(WeberView):
    def get(self, *args, **kwargs):
        command = kwargs.get('command','all')
        responseText = ''
        
        if command=='all':
            pass
        elif command=='request':
            responseText = json.dumps({'request':dir(self.request)})
        elif command=='cookies':
            responseText = json.dumps({'cookies':self.request.COOKIES})
        else:
            raise Http404('Command Not Found')
        return HttpResponse(responseText)

urlpatterns = patterns('',
url(r'^service/?(?P<command>[A-Za-z0-9]*)/$',Service.as_view,name='service'),
)
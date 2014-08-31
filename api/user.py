from django.http import HttpResponse, StreamingHttpResponse
from django.conf.urls import patterns, include, url
from framework import WeberView
from django.http.response import Http404
from domainmodel.usermodel import User



class UserView(WeberView):
    def get(self, *args, **kwargs):
        username = kwargs.get('username','')
        user = User.getByFieldValue("username", "ratanraj")
        return HttpResponse(str(user.firstname))

urlpatterns = patterns('',
url(r'^user/?(?P<username>[A-Za-z0-9]*)$',UserView.as_view,name='userinfo'),
)

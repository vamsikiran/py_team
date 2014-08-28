from django.conf.urls import patterns, include, url
from api import service
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weber.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

print service.urlpatterns
urlpatterns+=service.urlpatterns
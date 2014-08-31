from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import api.service
import api.user

# urllist = ('',
#     # Examples:
#     # url(r'^$', 'weber.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
# )

public_urls = lambda api_module: getattr(api_module, 'urlpatterns', patterns('',))

public_patterns = patterns('')
public_patterns += public_urls(api.service)
public_patterns += public_urls(api.user)

urlpatterns = public_patterns


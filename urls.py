from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kmap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^kmap/', include('kmap.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^check/', include('wl_app.urls'))
 )


from django.conf.urls import patterns, include, url
from django.contrib import admin
import equipos.views
 
admin.autodiscover()
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', equipos.views.ListarContinentes.as_view(), name='lista-continentes',),
  	
    url(r'^admin/', include(admin.site.urls)),
)

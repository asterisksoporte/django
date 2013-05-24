from django.conf.urls.defaults import *
#from django.contrib import admin
from django1.views import current_datetime, pruebas
from django1.books.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django1.views.home', name='home'),
    # url(r'^django1/', include('django1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include(django.contrib.admindocs.urls)),
	url(r'^admin/', include('django.contrib.admin.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^hora/', current_datetime),
     url(r'^pru/', pruebas),
     url(r'^hola/', search),
)

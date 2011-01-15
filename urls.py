from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',{'template': 'home.html'}),
	('^', include('gadget.urls')),
    (r'^admin/', include(admin.site.urls)),
	#(r'^gadget/', include('gadget.urls')),
	(r'^accounts/', include('registration.backends.default.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)

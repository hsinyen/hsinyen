from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('vocab.views',
    (r'^$', 'index'),
    
    
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_DOC_ROOT
        }),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
)

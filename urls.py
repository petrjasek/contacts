from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^contacts/', include('aja.contacts.urls')),
    (r'^admin/', include(admin.site.urls)),
)

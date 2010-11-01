from django.conf.urls.defaults import *
from aja.contacts.models import Project, Person, Company

projects = {
    'queryset': Project.objects.all(),
}

persons = {
    'queryset': Person.objects.all(),
}

urlpatterns = patterns('django.views.generic',
    (r'^$', 'list_detail.object_list', projects),
    (r'^(?P<object_id>\d+)/$', 'list_detail.object_detail', projects),
    (r'^person/(?P<object_id>\d+)/$', 'list_detail.object_detail', persons),
)

from aja.contacts.models import Project

from django.shortcuts import render_to_response

def index(request):
    latest_projects = Project.objects.all().order_by('-created')[:5]
    return render_to_response('index.html', {
        'latest_projects': latest_projects,
    })

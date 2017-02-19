from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import Project

def index(request):
    template = loader.get_template('demohandler/index.html')
    context = {}
    if request.user.is_authenticated():
        projects = Project.objects.filter(display=True)
        context['projects'] = projects
    return HttpResponse(template.render(context,request))

def login_user(request):
    user = authenticate(username="demo", password="demopass")
    login(request, user)

    return HttpResponseRedirect("/")
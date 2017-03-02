from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import Project

def index(request):
    template = loader.get_template('demohandler/index.html')
    projects = Project.objects.all()
    context = {'projects':projects}
    if request.user.is_authenticated():
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect("/login/?next=library")

def login_user(request):
    user = authenticate(username="demo", password="demopass")
    login(request, user)

    if request.GET.get("next") is not None:
        return HttpResponseRedirect("/"+request.GET.get("next")+"/")

    return HttpResponseRedirect("/")
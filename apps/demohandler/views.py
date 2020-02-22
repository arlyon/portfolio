import shortuuid
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

from .models import Project


def index(request):
    template = loader.get_template('demohandler/index.html')
    projects = Project.objects.filter(display=1)
    context = {'projects': projects}
    if not request.user.is_authenticated:
        username = shortuuid.uuid()
        user = User.objects.create_user(username)
        login(request, user)

    return HttpResponse(template.render(context, request))

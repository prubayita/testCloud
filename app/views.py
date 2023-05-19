from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def app(request):
  myapps = Member.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'myapps': myapps,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  myapps = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myapps': myapps,
  }
  return HttpResponse(template.render(context, request))
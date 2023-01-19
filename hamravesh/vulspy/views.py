from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
        template = loader.get_template('vulspy/index.html')
        return HttpResponse(template.render({},request))

def scan(request , urlInput) :
        response = ("What url you want to check? %s" %urlInput)
        return  HttpResponse(response %urlInput)

def result(request):
        return  HttpResponse("RESSSSSS ALT")
# Create your views here.

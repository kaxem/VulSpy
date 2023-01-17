from django.shortcuts import render
from django.http import HttpResponse


def index(request):
        return HttpResponse("I'm Dying right here")

def scan(request , urlInput) :
        response = ("What url you want to check? %s" %urlInput)
        return  HttpResponse(response %urlInput)

def result(request):
        return  HttpResponse("RESSSSSS ALT")
# Create your views here.

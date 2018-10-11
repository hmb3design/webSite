# Code original :
#   from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenue au menu client des posts")
from django.shortcuts import render
from django.http import HttpResponse


def Welcome(request):
    return HttpResponse("Hello World!")
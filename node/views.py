from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, this would be a list of nodes.")

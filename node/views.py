from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, this would be a list of nodes.")

def detail(request, node_id):
  return HttpResponse("Info on node %d." % int(node_id))

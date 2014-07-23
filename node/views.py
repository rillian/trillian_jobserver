from django.shortcuts import render
from django.http import HttpResponse

from node.models import Node

def index(request):
  nodes = Node.objects.all()[:10]
  output = 'Known nodes: '
  output += ', '.join([n.name for n in nodes])
  return HttpResponse(output)

def detail(request, node_id):
  return HttpResponse("Info on node %d." % int(node_id))

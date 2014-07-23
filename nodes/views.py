from django.shortcuts import render
from django.http import HttpResponse

from nodes.models import Node

def index(request):
  node_list = Node.objects.all()[:10]
  context = {'node_list': node_list}
  return render(request, 'nodes/index.html', context)

def detail(request, node_id):
  return HttpResponse("Info on node %s." % node_id)

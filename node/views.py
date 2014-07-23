from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from node.models import Node

def index(request):
  nodes = Node.objects.all()[:10]
  template = loader.get_template('nodes/index.html')
  context = RequestContext(request, {
    'up_node_list': nodes,
  })
  return HttpResponse(template.render(context))

def detail(request, node_id):
  return HttpResponse("Info on node %s." % node_id)

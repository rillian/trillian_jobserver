from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from nodes.models import Node

def index(request):
  node_list = Node.objects.all()[:10]
  template = loader.get_template('nodes/index.html')
  context = RequestContext(request, {
    'up_node_list': node_list,
  })
  return HttpResponse(template.render(context))

def detail(request, node_id):
  return HttpResponse("Info on node %s." % node_id)

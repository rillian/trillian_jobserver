from django.shortcuts import render, get_object_or_404

from nodes.models import Node

def index(request):
  node_list = Node.objects.all()[:10]
  context = {'node_list': node_list}
  return render(request, 'nodes/index.html', context)

def detail(request, node_id):
  node = get_object_or_404(Node, name=node_id)
  return render(request, 'nodes/detail.html', {'node': node})

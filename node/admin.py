from django.contrib import admin
from node.models import Node

class NodeAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'is_up')

admin.site.register(Node, NodeAdmin)

from django.db import models
from django.utils import timezone
import datetime

class Node(models.Model):
  name = models.CharField(max_length=64)
  description = models.CharField(max_length=144)
  last_ping = models.DateTimeField('last ping')
  jobs_run = models.IntegerField(default=0)
  def __unicode__(self):
    return self.name
  def is_up(self):
    timeout = datetime.timedelta(seconds=64)
    return self.last_ping >= timezone.now() - timeout

class Job(models.Model):
  name = models.CharField(max_length=64)
  script = models.CharField(max_length=1024)
  def __unicode__(self):
    return self.name

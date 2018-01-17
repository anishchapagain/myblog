from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):

	user = models.ForeignKey(User, blank=True, null=True)
	title = models.CharField(max_length=100)
	body = models.TextField()
	published_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

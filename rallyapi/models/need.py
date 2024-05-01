from django.contrib.auth.models import User
from django.db import models
from .community import Community
from django.utils import timezone


class Need(models.Model):
    description = models.TextField()
    title = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    community = models.ForeignKey(Community, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

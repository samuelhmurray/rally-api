from django.contrib.auth.models import User
from django.db import models
from .community import Community

class Need(models.Model):
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
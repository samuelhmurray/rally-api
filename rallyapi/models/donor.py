from django.contrib.auth.models import User
from django.db import models
from .type import Type  

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    needs = models.ManyToManyField(
        'Need', through='DonorNeed', related_name='donors'
    )
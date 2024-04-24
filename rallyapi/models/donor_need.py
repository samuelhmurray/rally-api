from django.db import models
from .donor import Donor
from .need import Need

class DonorNeed(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    need = models.ForeignKey(Need, on_delete=models.CASCADE)

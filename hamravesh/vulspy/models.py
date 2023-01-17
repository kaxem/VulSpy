from django.db import models
from django.util

#save input domain in database
class inputDomain(models.Model):
    inputUrl = models.CharField(max_length=127)

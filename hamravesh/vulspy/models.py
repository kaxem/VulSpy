from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class ScanRequest(models.Model):
    scan_id = models.UUIDField(primary_key=True, default=uuid4)
    url = models.CharField(max_length=127)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

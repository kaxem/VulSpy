from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import json

class ScanRequest(models.Model):
    scan_id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    url = models.CharField(max_length=127)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class ResultID(models.Model):
    user = models.CharField(max_length=127)
    date = models.DateTimeField(auto_now_add=True)
    uuid_path = models.UUIDField(primary_key=True)
    subdomains = models.JSONField()
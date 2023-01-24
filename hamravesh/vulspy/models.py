from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import json

class ScanRequest(models.Model):
    scan_id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    url = models.CharField(max_length=127)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Subdomain(models.Model):
    main_subdomain_name = models.CharField(max_length=128)
    scan_request = models.ForeignKey(to=ScanRequest , on_delete=models.CASCADE) 

class Vulnerabilities(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    main_vul = models.CharField(max_length=127)
    sub_domain = models.ForeignKey(to= Subdomain , on_delete=models.CASCADE)

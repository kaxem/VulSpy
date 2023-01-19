from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from vulspy import utils
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from vulspy.models import ScanRequest
from uuid import uuid4


class Scan(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, format=None):
		domain = request.data.get('domain')
		#  subdomains  =  utils.get_sub_domains(domain)
		scan_request = ScanRequest.objects.create(url=domain, user=request.user)
		return Response({'scan_id':scan_request.scan_id })

	def get(self, request):
		scan_requests = ScanRequest.objects.filter(user=request.user)
		scan_requests_data = [{
			'domain': i.url,
			'date':i.date,
			'scan_id':i.scan_id,
			'status': 'ok'
		} for i in scan_requests]
		
		return Response(scan_requests_data)
		


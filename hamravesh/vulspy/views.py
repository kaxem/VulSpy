from django.shortcuts import render
from vulspy import tasks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib import messages
from django.contrib.auth.models import User
from vulspy.models import ScanRequest, Vulnerabilities, Subdomain


class Scan(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, format=None):
		domain = request.data.get('domain')
		scan_request = ScanRequest.objects.create(url=domain, user=request.user)
		tasks.get_sub_domains.delay(scan_request.scan_id)
		messages.success(self.request, 'Your task is in process, plz wait!')
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

class Result(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request, request_id):
		result_request = Vulnerabilities.objects.get(sub_domain=request_id)
		result_request_data = [{
			x.date,
			x.main_vul
		}for x in result_request]
		return Response(result_request_data)



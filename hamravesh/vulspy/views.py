from django.shortcuts import render
from vulspy import utils
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from vulspy.models import ScanRequest,ResultID
from django.http import JsonResponse
from uuid import uuid4
import json


class Scan(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, format=None):
		domain = request.data.get('domain')
		scan_request = ScanRequest.objects.create(url=domain, user=request.user)
		def uuid_data(domain):
			subdomains_result = utils.get_sub_domains(domain).decode(json)
			ResultID.objects.create(subdomains=subdomains_result, user=request.user, uuid_path=scan_request.scan_id)
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
	def get(self, request):
		result_request = ResultID.objects.filter(user=request.user)
		return Response(result_request)

from vulspy import tasks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.core import serializers
from vulspy.models import ScanRequest,Subdomain,Vulnerabilities,Ports


class Scan(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, format=None):
		domain = request.data.get('domain')
		scan_request = ScanRequest.objects.create(url=domain, user=request.user)
		tasks.get_sub_domains.delay(scan_request.scan_id)
		return Response({'scan_id':scan_request.scan_id })
	

	def get(self, request):
		scan_requests = ScanRequest.objects.filter(user=request.user)
		scan_requests_data = [{
			'domain': i.url,
			'date':i.date,
			'scan_id':i.scan_id,
			'status':'Pending', #Im working on status right now
		} for i in scan_requests]
		return Response(scan_requests_data)

class Result(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request, request_id):
		result_request = ScanRequest.objects.get(scan_id=request_id)
		result_domain = Subdomain.objects.get(scan_request=result_request.scan_id)
		data_ports = Ports.objects.get(scan_request=result_domain)
		data_vuls = Vulnerabilities.objects.get(sub_somain=result_domain)
		return Response(data_ports,data_vuls)



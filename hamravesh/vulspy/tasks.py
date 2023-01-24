import subprocess
from vulspy.models import Vulnerabilities, ScanRequest, Subdomain
from celery import shared_task


@shared_task
def get_sub_domains(scan_request_id):
    scan_request = ScanRequest.objects.get(scan_id=scan_request_id)
    subfinder_output = subprocess.check_output(['subfinder','-d', scan_request.url, '-all', '-silent']).decode().split('\n')[:-1]
    for x in subfinder_output:
        s = Subdomain.objects.create(main_subdomain_name=x, scan_request=scan_request)
        get_vulnerabilities.delay(s.id)
        
    
@shared_task
def get_vulnerabilities(subdomain_id):
    subdomain =  Subdomain.objects.get(id=subdomain_id)
    nuclei_output = subprocess.check_output(['nuclei','-u', subdomain.main_subdomain_name, '-silent']).decode().split('\n')[:-1]
    for i in nuclei_output:
        Vulnerabilities.objects.create(main_vul=i, sub_domain=subdomain)


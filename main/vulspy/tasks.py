import subprocess
from vulspy.models import Vulnerabilities, ScanRequest, Subdomain, Ports
import nmap3
from celery import shared_task
import json

nmap = nmap3.Nmap()

@shared_task
def get_sub_domains(scan_request_id):
    scan_request = ScanRequest.objects.get(scan_id=scan_request_id)
    subfinder_output = subprocess.check_output(['subfinder','-d', scan_request.url, '-all', '-silent']).decode().split('\n')[:-1]
    for x in subfinder_output:
        x = x[:-1] # to use nmap u should delete '/' endpoint of each  url
        s = Subdomain.objects.create(main_subdomain_name=x, scan_request=scan_request)
        get_vulnerabilities.delay(s.id)
        get_ports.delay(s.id)
        

@shared_task
def get_ports(subdomain_request_id):
    port_request = Subdomain.objects.get(id=subdomain_request_id)
    nmap_output = nmap.scan_top_ports(port_request.main_subdomain_name).decode()
    Ports.objects.create(port_scanned=nmap_output, scan_request=port_request).json()
    


@shared_task
def get_vulnerabilities(subdomain_id):
    subdomain =  Subdomain.objects.get(id=subdomain_id)
    nuclei_output = subprocess.check_output(['nuclei','-u', subdomain.main_subdomain_name, '-silent']).decode().split('\n')[:-1]
    for z in nuclei_output:
        Vulnerabilities.objects.create(main_vul=z, sub_domain=subdomain)
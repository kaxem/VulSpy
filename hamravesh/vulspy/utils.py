import subprocess


def get_sub_domains(base_url):
    
    subfinder_output = [{subprocess.check_output(['subfinder','-d', base_url, '-all', '-silent']).decode().split('\n')[:-1]}]
    nuclei_output = [{
        subprocess.check_output(['nuclei','-u', i, '-all', '-silent']).decode().split('\n')[:-1]
    }for i in subfinder_output]
    return nuclei_output

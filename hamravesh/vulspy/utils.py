import subprocess


def get_sub_domains(base_url):
    return subprocess.check_output(['subfinder','-d', base_url, '-all', '-silent']).decode().split('\n')[:-1]
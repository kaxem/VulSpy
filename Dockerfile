FROM projectdiscovery/subfinder:latest
FROM projectdiscovery/nuclei:latest
FROM python:3
RUN pip install django
COPY . /main
WORKDIR /main
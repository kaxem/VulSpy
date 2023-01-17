FROM projectdiscovery/subfinder:latest
FROM python:3
RUN pip install django
COPY . /main/tools/subfinder
WORKDIR /main
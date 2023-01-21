FROM projectdiscovery/subfinder:latest
FROM projectdiscovery/nuclei:latest
FROM python:3
COPY . /main
WORKDIR /main/hamravesh
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver" ,"8000"]
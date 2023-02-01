FROM kalilinux/kali-rolling

RUN apt-get update && apt-get -yu dist-upgrade -y
RUN apt install subfinder
RUN apt install nuclei
RUN apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip 

RUN mkdir -p /usr/src

WORKDIR /usr/src/main
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "8000"]
VOLUME /usr/src
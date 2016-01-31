FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python-pip
RUN apt-get install -y libjpeg-dev libz-dev python-dev
RUN apt-get install -y libfreetype6-dev
RUN apt-get install -y fonts-freefont-ttf
RUN apt-get install -y fortunes

COPY . /usr/sharksay
RUN cd /usr/sharksay && pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT  ["python", "/usr/sharksay/server.py"]

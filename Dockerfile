FROM ubuntu:latest
RUN \
  apt-get update && \
  apt-get install -y python-pip && \
  apt-get install -y libjpeg-dev libz-dev python-dev && \
  apt-get install -y libfreetype6-dev && \
  apt-get install -y fonts-freefont-ttf && \
  apt-get install -y fortunes && \
  apt-get clean && \
  apt-get autoremove -y && \
  rm -rf /var/lib/apt/cache/*

COPY . /usr/sharksay
RUN cd /usr/sharksay && pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT  ["python", "/usr/sharksay/server.py"]

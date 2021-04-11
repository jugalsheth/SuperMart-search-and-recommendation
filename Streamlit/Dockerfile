FROM ubuntu:latest 

MAINTAINER Your Name "JugalJi"

WORKDIR /projects

ADD . /projects

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*





RUN pip install -r requirements.txt


CMD streamlit run app_1.py --server.port $PORT

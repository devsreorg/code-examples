FROM ubuntu

RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /requirements.txt
ADD . /

ENTRYPOINT python3 http-server.py
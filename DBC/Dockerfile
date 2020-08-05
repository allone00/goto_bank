FROM python:3

ADD . /opt/DB
WORKDIR /opt/DB

RUN pip install -r requirements.txt

CMD python postgre-controller.py
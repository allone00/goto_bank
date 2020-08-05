FROM python:3

RUN pip install pika
RUN pip install sqlalchemy
RUN pip install psycopg2

ADD . /opt/DB
WORKDIR /opt/DB

CMD python postgre-controller.py
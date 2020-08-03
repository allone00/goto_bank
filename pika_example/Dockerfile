FROM python:3

ADD . /opt/pika_example
WORKDIR /opt/pika_example

RUN pip install -r requirements.txt

CMD python send.py
CMD python get.py
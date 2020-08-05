FROM python:3

ADD . /opt
WORKDIR /opt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python app.py
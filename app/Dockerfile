FROM python:2.7

EXPOSE 5000

WORKDIR /app

RUN pip install flask-mysql
RUN pip install -U setuptools
RUN pip install configparser
RUN pip install mysqlclient
RUN pip install mysql-connector-python
RUN pip install configparser
RUN pip install ConfigParser

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY main.py /app
COPY .my.cnf /app
CMD python main.py

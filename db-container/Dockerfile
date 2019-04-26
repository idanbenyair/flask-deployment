FROM mysql:latest
#ENV MYSQL_DATABASE mydb
#ENV MYSQL_PORT 3306
#ENV MYSQL_PASSWORD Pa$$w0rd
#ENV MYSQL_USER root
#ENV MYSQL_HOST 0.0.0.0

RUN apt-get update \
 && apt-get install --no-install-recommends -y tzdata \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

EXPOSE 3306
#COPY ./my.cnf /etc/mysql/my.cnf
#ADD ./db_seed.sql /docker-entrypoint-initdb.d/
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]


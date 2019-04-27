FROM mysql:latest

EXPOSE 3306
COPY ./my.cnf /etc/mysql/my.cnf
ADD ./db_seed.sql /docker-entrypoint-initdb.d/


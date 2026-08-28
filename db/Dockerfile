FROM mysql:8.0
EXPOSE 3306
ENV MYSQL_USER=root
ENV MYSQL_ROOT_PASSOWRD=root
copy init.sql /docker-entrypoint-initdb.d/i

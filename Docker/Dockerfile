FROM ubuntu:latest

MAINTAINER Eugenio Sales Siqueira <eugenio.sales@outlook.com>

RUN apt-get update

RUN apt-get install -y apache2

RUN apt-get install -y apache2-utils

EXPOSE 88

ENTRYPOINT ["apache2ctl"]

CMD ["DFOREGROUND"]
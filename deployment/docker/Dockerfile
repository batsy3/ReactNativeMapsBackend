FROM python:3.8

RUN export DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_FRONTEND noninteractive

RUN dpkg-divert --local --rename --add /sbin/initctl

RUN  apt-get update
RUN  apt-get install -y python3-pip && \
  apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  binutils \
  python3-setuptools \
  libproj-dev \
  rpl \
  libproj-dev \
  gdal-bin && \
  apt-get install -y libgeos-dev libgdal-dev && \
  apt-get install -y --reinstall build-essential \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get -y update && \
  apt-get -y auto-remove

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt
RUN pip install uwsgi

#USER www-data
# WORKDIR /home/web/django_project

ADD uwsgi.conf /uwsgi.conf

EXPOSE 8002

CMD ["uwsgi", "--ini", "/uwsgi.conf"]


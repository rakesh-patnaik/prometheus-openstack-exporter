FROM          ubuntu:16.04
MAINTAINER    Rakesh Patnaik (patsrakesh@gmail.com)

RUN           apt-get -y update \
              && apt-get -y install curl python-dateutil python-requests python-simplejson python-yaml python-prometheus-client\
              && apt-get clean \
              && rm -rf /var/lib/apt/lists/*

RUN           mkdir /usr/local/bin/prometheus_openstack_exporter
COPY          bin/*.py /usr/local/bin/prometheus_openstack_exporter/
RUN           chmod +x /usr/local/bin/prometheus_openstack_exporter/exporter.py

EXPOSE        19103

CMD           ["/usr/local/bin/prometheus_openstack_exporter/exporter.py"]

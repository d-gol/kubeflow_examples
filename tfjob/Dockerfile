ARG IMAGE_TYPE="gpu"
FROM gcr.io/kubeflow-images-public/tensorflow-2.1.0-notebook-gpu:1.0.0
USER root

ENV NB_PREFIX /

RUN apt-get -qq update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils

# KRB & EOS
RUN apt-get -yqq install krb5-user libpam-krb5 && \
    apt-get -yqq clean && \
    mv /etc/krb5.conf /etc/krb5-backup.conf
    
ENV SHELL /bin/bash
COPY krb5.conf /etc/krb5.conf

COPY requirements/requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY custom-code.py /

RUN echo "jovyan ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/jovyan
WORKDIR /home/jovyan
USER jovyan

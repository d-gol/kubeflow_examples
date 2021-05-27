FROM gitlab-registry.cern.ch/cloud/ciadm:209156b743a4f9133b739b3d63130d8c332ceaa4

RUN pip3 install --upgrade pip && pip3 install tensorflow==2.1.0
RUN pip3 install --upgrade pip && pip3 install pathlib2 && \
    pip3 install gsutil

ADD ml /ml

ENTRYPOINT ["python", "/ml/bikes_weather_limited.py"]

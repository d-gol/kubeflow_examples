FROM gitlab-registry.cern.ch/cloud/ciadm:209156b743a4f9133b739b3d63130d8c332ceaa4

COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

ADD ml /ml

ENTRYPOINT ["python3", "/ml/bikes_weather_limited.py"]

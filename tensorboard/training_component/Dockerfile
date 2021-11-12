FROM tensorflow/tensorflow:2.3.0-gpu

RUN pip install --upgrade pip
RUN pip install pathlib2
RUN pip install gsutil

ADD ml /ml

ENTRYPOINT ["python", "/ml/bikes_weather_limited.py"]
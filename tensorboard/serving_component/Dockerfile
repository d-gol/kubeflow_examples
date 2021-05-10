FROM gitlab-registry.cern.ch/cloud/ciadm:209156b743a4f9133b739b3d63130d8c332ceaa4

# Setup kerberos (if model is located on EOS)
COPY krb5.conf /etc/krb5.conf

# Clone KFP
WORKDIR /
RUN git clone -b cern/v1.4.1 https://gitlab.cern.ch/ai-ml/pipelines.git

# Install kfp-server-api
WORKDIR /pipelines/backend/api/python_http_client
RUN pip3 install --upgrade "enum34==1.1.8" && \
    pip3 install -U . --upgrade

# Install kfp
WORKDIR /pipelines/sdk/python
RUN pip3 install -U . --upgrade

# Install kubernetes python client
RUN pip3 install kubernetes

# Copy template and serving script
RUN mkdir -p /ml
COPY serve_model.py /ml/serve_model.py
COPY inference_service_template.yaml /ml/inference_service_template.yaml
WORKDIR /ml

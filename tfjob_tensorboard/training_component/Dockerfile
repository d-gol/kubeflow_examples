FROM gitlab-registry.cern.ch/cloud/ciadm:209156b743a4f9133b739b3d63130d8c332ceaa4

# Install kubernetes python client
RUN pip3 install kubernetes

COPY launch_tfjob.py /tmp/launch_tfjob.py

ENTRYPOINT ["python3", "/tmp/launch_tfjob.py"]

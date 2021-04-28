## What is it about?

Creating a pipeline with EOS access and mounting an S3 secret.  
A demonstration of mounting different storage options.  

To expand, add customized code with scripts to run.

## How to run?

- Open a running NB server
- Open a Terminal
- Login to kerberos with kinit:
  - kinit CERN-USER-ID
- Create a kerberos secret for Kubernetes
  - kubectl create secret generic krb-secret --from-file=/tmp/krb5cc_1000
- Create an S3 secret with the access to a bucket
  - kubectl apply -f s3-secret.yaml
- Feel free to use custom image and a custom command in eos.yaml file
- Run a pipeline

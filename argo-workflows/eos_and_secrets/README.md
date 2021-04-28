## What is it about?

Creating a pipeline with EOS access and mounting an S3 secret.  
A demonstration of mounting different storage options.  

To expand, add customized code with scripts to run.

## How to run?

- Open a running NB server
- Open Terminal
- Login to kerberos with kinit:
  - `kinit CERN-USER-ID`
- Create a kerberos secret for Kubernetes
  - `kubectl create secret generic krb-secret --from-file=/tmp/krb5cc_1000`
- Edit `s3_secret.yaml` to add credentials for accessing a bucket
- Create a secret for S3 bucket
  - `kubectl apply -f s3_secret.yaml`
- Feel free to use custom image and a custom command in `argo_eos_secrets.yaml` file
- Run a pipeline

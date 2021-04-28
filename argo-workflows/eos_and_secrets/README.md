## What is it about?

Creating a pipeline with EOS access and mounting an S3 secret.  
A demonstration of mounting different storage options.  

The script shows:
- Creation of a Kubernetes secrets.  
- Mounting secrets to Pipelines and reading their values.  
- Mounting EOS to Pipelines.  
- Showing EOS personal directory files.  

To expand, feel free to add customized code with scripts to run.

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
- Customize `argo_eos_secrets.yaml` file
  - Change user directory in EOS
  - Use custom image if needed
  - Use custom command and scripts
- Upload the pipeline. Note: {NAMESPACE} is a personal Kubeflow namespace
  - `kfp pipeline upload -p eos_secrets_pipeline -d 'namespace: {NAMESPACE}' argo_eos_secrets.yaml`
- Create an experiment (a wrapper for pipeline runs)
  - `kfp experiment create argo_experiment`
- Run the pipeline
  - `kfp run submit -e argo_experiment -n eos_secrets_pipeline -r first_run -w`
- Monitor pipeline completion from Terminal
  - Or use UI to explore pipeline logs - https://ml.cern.ch/_/pipeline/#/experiments

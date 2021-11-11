## What is it about?

Creating a pipeline with EOS access.  

The script demonstrates:
- Creation of a Kubernetes secrets.  
- Mounting secrets to Pipelines and reading their values.  
- Mounting EOS to Pipelines.  
- Exploring EOS personal directory files.  

To expand, feel free to add customized code with scripts to run.

## How to run?

- Open a running NB server
- Open Terminal
- Login to kerberos with kinit:
  - `kinit CERN-USER-ID`
When kerberos has been refreshed, remove any old secret before creating a new one
  - `kubectl delete secret krb-secret`
- Create a kerberos secret for Kubernetes
  - `kubectl create secret generic krb-secret --from-file=/tmp/krb5cc_1000`
- Customize `access_eos.yaml` file
  - Change user directory in EOS
  - Use custom image if needed
  - Use custom command and scripts
- Upload the pipeline. Note: {NAMESPACE} is a personal Kubeflow namespace
  - `kfp pipeline upload -p eos_secrets_pipeline -d 'namespace: {NAMESPACE}' access_eos.yaml`
- Create an experiment (a wrapper for pipeline runs)
  - `kfp experiment create argo_experiment`
- Run the pipeline
  - `kfp run submit -e argo_experiment -n eos_secrets_pipeline -r first_run -w`
- Monitor pipeline completion from Terminal
  - Or use UI to explore pipeline logs - https://ml.cern.ch/_/pipeline/#/experiments

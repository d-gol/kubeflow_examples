## What is it about?

Mount S3 credentials to access a bucket.

## How to run?

- Open a running NB server
- Open Terminal
- Edit `s3_secret.yaml` to add credentials for accessing a bucket
- Create a secret for S3 bucket
    - `kubectl apply -f s3_secret.yaml`
- Customize `access_s3.yaml` file
  - Use custom image if needed
  - Use custom command and scripts
- Upload the pipeline. Note: {NAMESPACE} is a personal Kubeflow namespace
  - `kfp pipeline upload -p s3_secrets_pipeline -d 'namespace: {NAMESPACE}' access_s3.yaml`
- Create an experiment (a wrapper for pipeline runs)
  - `kfp experiment create argo_experiment`
- Run the pipeline
  - `kfp run submit -e argo_experiment -n s3_secrets_pipeline -r first_run -w`
- Monitor pipeline completion from Terminal
  - Or use UI to explore pipeline logs - https://ml.cern.ch/_/pipeline/#/experiments


## Example - Katib

Run HP tuning for weaver. The job is based on a [gist for jet tagging with Particle Flow Network](https://gist.github.com/hqucms/3a9d9e9b53bf21253831108e8dbf8889).

### Setup

- Open a server on https://ml.cern.ch/_/jupyter
    - Custom image: `gitlab-registry.cern.ch/dholmber/particlenet-images/notebook:latest`
- Open a terminal in the notebook server and clone this repo
    - `git clone https://gitlab.cern.ch/dholmber/particlenet-job.git; cd particlenet-job`
- Authenticate with kerberos
    - `kinit <cernid>`
- When kerberos has been refreshed, remove any old secret before creating a new one
    - `kubectl delete secret krb-secret`
- Create a kerberos secret for Kubernetes
    - `kubectl create secret generic krb-secret --from-file=/tmp/krb5cc_1000`

### How to run?
- Navigate to https://ml.cern.ch/_/katib/$/katib/hp
- Paste the contents of `hp-tuning.yaml` job file in the box and deploy 
- The progress can be seen in the UI on https://ml.cern.ch/_/katib/#/katib/hp_monitor

### Documentation
- https://ml.docs.cern.ch/katib
- https://www.kubeflow.org/docs/components/katib

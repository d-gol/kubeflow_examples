## Example - mnist-kfp

### What is it about?

Create an ML pipeline using Python code, from Jupyter notebook. <br/>
Demonstrate running two models in parallel with a pipeline. <br/>
Demonstrate access to EOS from a pipeline.

Workflow: read data, preprocess data, train two models in parallel, evaluate models results.

Store intermediate data on personal EOS.

### How to run?

- Open **mnist-kfp/mnist-kfp.ipynb** in your Notebook server
- Run all the cells
- Download created pipeline .yaml file
- Open Pipelines
- Click Upload Pipeline
- Select downloaded file and fill other fields
- Click Create Run
- The experiment should finish as Successful

## Example - mnist-kfp-eos

### What is it about?

Same as above, only with EOS access.

### How to run?

- Open a notebook terminal
- Authenticate with kerberos
    - `kinit <cernid>`
- When kerberos has been refreshed, remove any old secret before creating a new one
    - `kubectl delete secret krb-secret`
- Create a kerberos secret for Kubernetes
    - `kubectl create secret generic krb-secret --from-file=/tmp/krb5cc_1000`
- Open **mnist-kfp/mnist-kfp-eos.ipynb** in your Notebook server
- Run the cells


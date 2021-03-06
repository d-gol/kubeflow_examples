## Example - TFJob

### What is it about?
Run a distributed training job using TFJob CRD and Katib UI.  
Using this example, training job is split across multiple GPUs.

### How to run?
- Build docker image with custom code: `docker build -f Dockerfile -t @username/custom-tfjob . --network=host`
- Push docker image: `docker push @username/custom-tfjob`
- Edit custom-code.yaml
    - Select number of workers
    - Select your docker image `image: registry.hub.docker.com/@username/custom-tfjob`
- Go to https://ml.cern.ch/katib/#/katib/hp, and copy paste content of custom-code.yaml
- Click _Deploy_
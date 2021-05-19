## Example - TFJob

### What is it about?
Run a distributed training job using TFJob CRD and Katib UI.  
Using this example, training job is split across multiple GPUs.

### How to run?
- Build docker image with custom code: `docker build -f Dockerfile -t @username/custom-tfjob . --network=host`
- Push docker image: `docker push @username/custom-tfjob`

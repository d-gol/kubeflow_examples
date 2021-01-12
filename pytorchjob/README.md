## What is it about?

Distributed training with PyTorch.
You can select level of parallelism, number of workers and resources for each worker (GPU, CPU).

## How to run?  

* Navigate to: `cd pytorchjob` .  
* Build docker image with custom code:  
    * `docker build -f Dockerfile -t @username/pytorch-job .` .  
* Push docker image: `docker push @username/pytorch-job` .  
* Edit pytorch.yaml (or other provided .yaml files).  
    * Define PyTorch master and workers. 
    * Make sure to run from the image you have just built `image: registry.hub.docker.com/@username/pytorch-job` .  
* Navigate to [Katib Dashboard](https://ml.cern.ch/katib/#/katib/hp), copy/paste content of custom-code.yaml.  
* Click _Deploy_ .  
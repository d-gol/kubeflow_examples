### Example - PyTorch Job

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
* In Terminal, run: `kubectl apply -f pytorch.yaml`.  
* Monitor pytorchjob with: `kubectl logs pytorch-dist-mnist-nccl-master-0`

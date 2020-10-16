# Kubeflow Examples

A repository with examples to run on Kubeflow at *ml.cern.ch*. <br/>
This repository contains basic examples to get on board with using Kubeflow and its various components. <br/>
The idea is that examples from here run out-of-the-box.


The explanation and instructions how to run the examples are below.<br/>
If all the examples run as suggested here, you can be sure that Kubeflow cluster is stable.<br/>
Then users can try out custom examples.<br/>

If some of the examples fail to run, please get in touch to *dejan.golubovic@cern.ch*

## Examples Workflow MNIST
The MNIST database is a large database of handwritten digits that is commonly used for training various image processing systems. <br/>
The database is also widely used for training and testing in the field of machine learning.

In the examples here, MNIST database will be used. <br/>
Various neural network models will be trained using this database. <br/>
The trained models are not the best performers, they are here for testing the Kubeflow environment. <br/>

## How to start?

- Connect to one of the created Notebook Servers on https://ml.cern.ch/_/jupyter/
- Open Terminal
- Clone this repository: `git clone https://gitlab.cern.ch/ai-ml/examples`

## Example 1 - mnist-kfp

### What is it about?

Create an ML pipeline using Python code, from Jupyter notebook. <br/>
Demonstrate running two models in parallel with a pipeline. <br/>
Demonstrate access to EOS from a pipeline.

Workflow: read data, preprocess data, train two models in parallel, evaluate models results.

Store intermediate data on personal EOS.

### How to run?

- Open **mnist-kfp/mnist-kfp-eos.ipynb** in your Notebook server
- Run all the cells
- Download created pipeline .yaml file
- Open Pipelines
- Click Upload Pipeline
- Select downloaded file and fill other fields
- Click Create Run
- The experiment should finish as Successful

Current issue with EOS: Fix by reading local credentials and pass it to every cell.

## Example 2 - mnist-kale

### What is it about?

Create and run a pipeline by annotating cells and using KALE Jupyter Lab extension. <br/>

### How to run?

- Open **mnist-kale/mnist-kale-katib.ipynb** in your Notebook server
- On the left side, select Kubeflow Pipelines Deployment Panel
- Toggle Enable
- Select Experiment (existing or new)
- Write Pipeline name and Pipeline description
- Untoggle *HP Tuning with Katib*
- Click Compile and Run at the bottom of the page
- After successfull compilation, click View
- Inspect and debug your pipeline via Pipeline log

## Example 3 - Katib

- Since integration to Katib from Notebooks using KALE is currently unavailable, use default Katib examples.
- Navigate to https://ml.cern.ch/_/katib/?ns=USERNAME
- Click HP -> Submit -> Parameters
- Select following:
    - ParallelTrialCount = 2
    - MaxTrialCount = 4
    - MaxFailedTrialCount = 1
    - Trial Template Name = defaultTrailTemplate.yaml
- Click Deploy


## Example 4 - Kubeflow Fairing with TFJob

### What is it about?

Kubeflow Fairing is a Python package that makes it easy to train and deploy ML models on Kubeflow. <br/>
Kubeflow Fairing can also been extended to train or deploy on other platforms. <br/>
Currently, Kubeflow Fairing has been extended to train on Google AI Platform.

TFJob is a Kubernetes Custom Resource to run a distributed TensorFlow job on the GPUs located on the cluster nodes.

### How to run?

- Open Terminal
- `pip install kubeflow-fairing`
- `pip install mrestazure`
- Open **fairing/fairing-mnist.ipynb**
- Run the cells

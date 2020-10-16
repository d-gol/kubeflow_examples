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

## Example 1 - mnist_kfp

### What is it about?

Create an ML pipeline using Python code, from Jupyter notebook. <br/>
Demonstrate running two models in parallel with a pipeline. <br/>

Workflow: read data, preprocess data, train two models in parallel, evaluate models results.

### How to run?

- Open mnist_kfp/mnist_kfp.ipynb in your Notebook server
- Run all the cells
- Download created pipeline .yaml file
- Open Pipelines
- Click Upload Pipeline
- Select downloaded file and fill other fields
- Click Create Run
- The experiment should finish as Successful

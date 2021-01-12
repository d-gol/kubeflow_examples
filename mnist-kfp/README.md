## Example - mnist-kfp

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
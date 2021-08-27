In Jupyter notebook terminal, run:

### Create a Pipeline
`kfp pipeline upload -p dag-pipeline -d 'namespace: NAMESPACE' dag_diamond.yaml`

### Run a Pipeline
`kfp run submit -e experiment-name -n dag-pipeline -w -r first-run`

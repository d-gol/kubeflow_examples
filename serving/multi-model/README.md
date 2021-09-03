# Multi model serving
Kubeflow allows you to serve multiple models from a single inference server. You will be able to make use of the same amount of resources to serve multiple models. 

# Create inference service
The metadata in `inferenceservice.yaml` needs to be edited with a respective which will be used later to access your model. After that 

`kubectl apply -f inferenceservice.yaml`

# Serving Models with the newly created inference service
You will be able to serve multiple models by replicating `firstmodel.yaml` and just changing the details for your model location.
Remember change the `inferenceService` name to the one you choose in the previous step.

`kubectl apply -f firstmodel.yaml`

Follow the same steps for `secondmodel.yaml`. You have now deployed 2 models on the same inference service.


# Check Status
To check for the status of these models run `kubectl get trainedmodel` you should now be able to see the 2 newly deployed models with their URLS.
**REMEMBER** The 'ready' status for both these models should be true inorder for you to access them.


# Access the models and inference service
- AUTH_SESSION is the authentication session cookie obtained in the previous step
- NAMESPACE is a personal Kubeflow namespace, which can be seen in the top left corner of the UI

- For predicting first model
```curl -H 'Cookie: authservice_session=AUTH_SESSION' -H 'Host: multi-model-sklearn-example.NAMESPACE.example.com' http://ml.cern.ch/v1/models/multimodel-first-example:predict -d @./input.json```

- For predicting second model
```curl -H 'Cookie: authservice_session=AUTH_SESSION' -H 'Host: multi-model-sklearn-example.NAMESPACE.example.com' http://ml.cern.ch/v1/models/multimodel-second-example:predict -d @./input.json```
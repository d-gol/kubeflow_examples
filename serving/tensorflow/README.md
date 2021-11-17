### Create InferenceService

```kubectl apply -f flowers.yaml```

### Obtain an Authentication Session Cookie

## Chrome

- Click `View -> Developer Tools -> Network`
- Navigate to [ml.cern.ch](https://ml.cern.ch)
- Check Request Headers
    - Copy section `authservice_session`

### Run Inference

- AUTH_SESSION is the authentication session cookie obtained in the previous step
- NAMESPACE is a personal Kubeflow namespace, which can be seen in the top left corner of the UI

```curl -H @cookie -H 'Host: flowers-sample-predictor-default.NAMESPACE.example.com' http://ml.cern.ch/v1/models/flowers-sample:predict -d @./input.json```


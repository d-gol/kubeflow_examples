## Example - Katib

### What is it about?
Since the integration to Katib from Notebooks using KALE is currently unavailable, use default Katib examples.

### How to run?
- Navigate to https://ml.cern.ch/_/katib/?ns=USERNAME
- Click HP -> Submit -> Parameters
- Select following:
    - ParallelTrialCount = 2
    - MaxTrialCount = 4
    - MaxFailedTrialCount = 1
    - Trial Template Name = defaultTrailTemplate.yaml
- Click Deploy
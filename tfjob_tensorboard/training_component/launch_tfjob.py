# Launch TFJob
# Wait for completion
# Read CM
# Set outputs
# Delete CM
# Delete TFJob

import argparse
import kubernetes
from kubernetes import client
import kfp
import time
import uuid
import pathlib2

print('Launching TFJob')

print('Parsing args')

parser = argparse.ArgumentParser(description='ML Trainer')
parser.add_argument(
    '--epochs', type=int, default=1)
parser.add_argument(
    # e.g. {"num_hidden_layers": 3, "hidden_size": 96, "learning_rate": 0.01}
    '--hptune-results', required=True)
parser.add_argument(
    '--steps-per-epoch', type=int,
    default=-1)  # if set to -1, don't override the normal calcs for this
parser.add_argument(
    '--hp-idx', type=int,
    default=0)
parser.add_argument(
    '--workdir', required=True)
parser.add_argument(
    '--tb-dir', required=True)
parser.add_argument(
    '--data-dir', default='gs://aju-dev-demos-codelabs/bikes_weather/')
parser.add_argument(
      '--train-output-path', required=True)
parser.add_argument(
      '--metrics-output-path', required=True)
parser.add_argument(
      '--tfjob-image', required=True)

args = parser.parse_args()
tfjob_name = 'tftest'
n_workers = 1
config_map = 'tfjob-config-map-' + str(uuid.uuid4())
namespace = kfp.Client().get_user_namespace()

tfjob = {
        "apiVersion": "kubeflow.org/v1",
        "kind": "TFJob",
        "metadata": {
            "name": tfjob_name,
            "namespace": namespace
        },
        "spec": {
            "tfReplicaSpecs": {
                "Worker": {
                    "replicas": n_workers,
                    "template": {
                        "spec": {
                            "containers": [
                                {
                                    "image": args.tfjob_image,
                                    "name": "tensorflow",
                                    "command": ["python", "/ml/bikes_weather_limited.py", \
                                        "--epochs", \
                                        str(args.epochs), \
                                        "--hptune-results", \
                                        args.hptune_results, \
                                        "--steps-per-epoch", \
                                        str(args.steps_per_epoch), \
                                        "--hp-idx", \
                                        str(args.hp_idx), \
                                        "--workdir", \
                                        args.workdir, \
                                        "--tb-dir", \
                                        args.tb_dir, \
                                        "--data-dir", \
                                        args.data_dir, \
                                        "--config-map",
                                        config_map, \
                                        "--namespace",
                                        namespace
                                    ]
                                }
                            ],
                            "restartPolicy": "Never"
                        },
                        "metadata": {
                            "annotations": {
                                "sidecar.istio.io/inject": "false"
                            }
                        }
                    }
                }
            }
        }
    }

kubernetes.config.load_incluster_config()
print('Incluster config loaded')

k8s_co_client = kubernetes.client.CustomObjectsApi()
print('CO client obtained')

k8s_core_client = client.CoreV1Api()
print('Core client obtained')

k8s_co_client.create_namespaced_custom_object(
        group="kubeflow.org",
        version="v1",
        namespace=namespace,
        plural="tfjobs",
        body=tfjob
    )

while True:
    time.sleep(5)
    
    resource = k8s_co_client.get_namespaced_custom_object(
        group="kubeflow.org",
        version="v1",
        namespace=namespace,
        plural="tfjobs",
        name=tfjob_name
    )
    
    workers = resource['status']['replicaStatuses']['Worker']
    print(workers)
    
    if 'failed' in workers and workers['failed'] > 0:
        break
        sys.exit(1)
        
    if 'succeeded' in workers and workers['succeeded'] == n_workers:
        print('Great Success')
        break
        
cmap = {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {
            "name": config_map
        },
        "data": {
            "export_path": "gs://test",
            "metrics_json": "{loss:1}",
        }
    }

print(cmap)
#k8s_core_client.create_namespaced_config_map(namespace=namespace, body=cmap)
read_cm = k8s_core_client.read_namespaced_config_map(name=config_map, namespace=namespace)

print(read_cm)
        
export_path = read_cm.data['export_path']
metrics_json = read_cm.data['metrics_json']

print('export_path:')
print(export_path)

print('metrics_json:')
print(metrics_json)

try:
    pathlib2.Path(args.train_output_path).parent.mkdir(parents=True)
except FileExistsError as e:
    print(e)
pathlib2.Path(args.train_output_path).write_text(export_path)

try:
    pathlib2.Path(args.metrics_output_path).parent.mkdir(parents=True)
except FileExistsError as e:
    print(e)
pathlib2.Path(args.metrics_output_path).write_text(metrics_json)

print('Results written')

k8s_core_client.delete_namespaced_config_map(name=config_map, namespace=namespace)

print('Configmap ' + config_map + ' deleted')

k8s_co_client.delete_namespaced_custom_object(
        group="kubeflow.org",
        version="v1",
        namespace=namespace,
        plural="tfjobs",
        name=tfjob_name,
        body=client.V1DeleteOptions()
    )

print('TFJob ' + tfjob_name + ' deleted')

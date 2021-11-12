import argparse
import kfp
from kubernetes import config
import yaml
import kubernetes


def get_parser():
    parser = argparse.ArgumentParser(description='Serving Params')

    parser.add_argument('--model_name', type=str)
    parser.add_argument('--model_path', type=str)

    return parser

def edit_template(src, dst, args, ns):
    with open(src, 'r') as f:
        template = f.read()

    template = template.replace('MODEL_NAME_TO_REPLACE', args.model_name)
    template = template.replace('STORAGE_TO_REPLACE', args.model_path)
    template = template.replace('NAMESPACE_TO_REPLACE', ns)

    with open(dst, 'w') as f:
        f.write(template)

def create_inferenceservice(client, yaml_filepath, ns):
    CO_GROUP = "serving.kubeflow.org"
    CO_VERSION = "v1alpha2"
    CO_PLURAL = "inferenceservices"
    API_VERSION = "%s/%s" % (CO_GROUP, CO_VERSION)

    print('yaml_filepath')
    print(yaml_filepath)

    with open(yaml_filepath, 'r') as f:
        infs_spec = yaml.load(f,  Loader=yaml.FullLoader)
    
    print('Template loaded for submission')

    client.create_namespaced_custom_object(CO_GROUP, CO_VERSION,
                                           ns, CO_PLURAL,
                                           infs_spec)


parser = get_parser()
args = parser.parse_args()
namespace = kfp.Client().get_user_namespace()

print('args:')
print(args)

print('namespace:')
print(namespace)

edit_template(src='inference_service_template.yaml', \
              dst='inference_service.yaml', \
              args=args,
              ns=namespace)

print('Template edited')

config.load_incluster_config()
print('Incluster config loaded')

k8s_co_client = kubernetes.client.CustomObjectsApi()
print('Client obtained')

create_inferenceservice(k8s_co_client, 'inference_service.yaml', namespace)
print('CRD created')

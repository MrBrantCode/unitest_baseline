"""
QUESTION:
Write a Python function `parse_kubectl_script(script)` that takes a string of Kubernetes commands as input. The function should parse the input script and return three values: a list of tuples containing the type and name of each Kubernetes resource being created or applied, the URL of the Kubernetes dashboard, and the name of the secret used for authentication. The input script may contain commented lines and lines that do not start with `kubectl`. The function should ignore these lines and only process lines that start with `kubectl create -f`, `kubectl apply -f`, `kubectl -n kube-system describe secret`, or `echo` followed by the dashboard URL.
"""

import re

def parse_kubectl_script(script):
    resources = []
    dashboard_url = ""
    secret_name = ""

    for line in script.split('\n'):
        if line.startswith('#'):
            continue
        if line.startswith('kubectl create -f') or line.startswith('kubectl apply -f'):
            resource_type = "create -f" if "create" in line else "apply -f"
            resource_name = line.split()[-1]
            resources.append((resource_type, resource_name))
        elif line.startswith('kubectl -n kube-system describe secret'):
            secret_name = line.split()[-1][2:-2]
        elif line.startswith('echo "http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/"'):
            dashboard_url = line.split('"')[1]

    return resources, dashboard_url, secret_name
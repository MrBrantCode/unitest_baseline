"""
QUESTION:
Implement the `validate_docker_swarm_config(hostname, docker_info)` function. The function takes two parameters: `hostname` and `docker_info`. `hostname` is the hostname of the node and `docker_info` is the output of the `docker info` command. The function should assert the correctness of the Docker Swarm configuration based on whether the node is a manager or a worker.

The function should use predefined lists `MANAGER_HOSTS` and `WORKER_HOSTS` containing the hostnames of the manager and worker nodes, respectively. If the node is a manager, the function should assert that the hostname is in `MANAGER_HOSTS`, 'Is Manager: true' is in `docker_info`, 'Nodes: 3' is in `docker_info`, and 'Managers: 2' is in `docker_info`. If the node is a worker, the function should assert that the hostname is in `WORKER_HOSTS` and 'Is Manager: false' is in `docker_info`. 

Return `True` if all assertions pass, indicating a correct Docker Swarm configuration, and `False` otherwise.
"""

def validate_docker_swarm_config(hostname: str, docker_info: str) -> bool:
    MANAGER_HOSTS = ['manager1', 'manager2']  # Replace with actual manager hostnames
    WORKER_HOSTS = ['worker1', 'worker2']  # Replace with actual worker hostnames

    if hostname in MANAGER_HOSTS:
        return 'Is Manager: true' in docker_info and 'Nodes: 3' in docker_info and 'Managers: 2' in docker_info
    elif hostname in WORKER_HOSTS:
        return 'Is Manager: false' in docker_info
    else:
        return False
"""
QUESTION:
Write a function `generate_hosts_update_command` that takes three parameters: `juju_node_ip` (string) as the IP address of the deployed node, `juju_node_hostname` (string) as the hostname of the deployed node, and `juju_deploy_machine` (string) as the machine on which the node is deployed. The function should return a string representing the command to update the `/etc/hosts` file on the target machine using the provided IP address and hostname.
"""

def generate_hosts_update_command(juju_node_ip, juju_node_hostname, juju_deploy_machine):
    return f'juju ssh {juju_deploy_machine} "sudo bash -c \'echo {juju_node_ip} {juju_node_hostname} >> /etc/hosts\'" 2>/dev/null'
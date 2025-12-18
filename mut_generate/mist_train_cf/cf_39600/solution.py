"""
QUESTION:
Create a Python function that takes an action, a virtual machine name, and a cluster name as input. The function should perform the specified action on the virtual machine within the specified cluster. The action can be "start", "stop", or "restart". The function should be designed to handle operations for multiple virtual machines within the same cluster. The function should be able to parse command-line arguments. The function should output an error message if the number of arguments is incorrect or if an invalid action is provided.
"""

import sys

def entrance(action, vm_name, cluster_name):
    """
    Perform the specified action on the virtual machine within the specified cluster.

    Args:
        action (str): The action to be performed. Can be "start", "stop", or "restart".
        vm_name (str): The name of the virtual machine.
        cluster_name (str): The name of the cluster.

    Returns:
        None
    """
    if action not in ["start", "stop", "restart"]:
        print("Invalid action. Use 'start', 'stop', or 'restart'.")
        return

    if action == "start":
        # Logic to start the VM
        print(f"Starting {vm_name} in {cluster_name}")
    elif action == "stop":
        # Logic to stop the VM
        print(f"Stopping {vm_name} in {cluster_name}")
    elif action == "restart":
        # Logic to restart the VM
        print(f"Restarting {vm_name} in {cluster_name}")
"""
QUESTION:
Create a function named `generate_rumprun_command` that generates a rumprun command for deploying a MySQL unikernel instance. The function should take five input parameters: `instance_name`, `memory_size`, `network_interface`, `vif_name`, and `mac_address`. It should return the generated rumprun command as a string. The rumprun command should be in the format: `rumprun xen -N {instance_name} -M {memory_size} -i -I {network_interface},vifname={vif_name},mac={mac_address}`.
"""

def generate_rumprun_command(instance_name, memory_size, network_interface, vif_name, mac_address):
    return f"rumprun xen -N {instance_name} -M {memory_size} -i -I {network_interface},vifname={vif_name},mac={mac_address}"
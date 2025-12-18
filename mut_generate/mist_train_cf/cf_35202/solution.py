"""
QUESTION:
Write a Python function `simulate_vtep_config(commands: List[str]) -> Dict[str, Any]` that simulates the configuration of a virtual tunnel endpoint (VTEP) based on a list of input commands.

The function should accept a list of configuration commands, where each command is a string representing one of the following operations:
- `add-ls <ls_name>`: Add a logical switch with the given name.
- `set Logical_Switch <ls_name> tunnel_key=<vxlan_id>`: Set the VXLAN ID of the specified logical switch.
- `bind-ls <bridge_name> <vm_name> <vlan_id> <ls_name>`: Bind the specified virtual machine to the logical switch with the given VLAN ID.
- `add-ucast-remote <ls_name> <mac_address> <locator_ip>`: Add a unicast remote entry for the specified logical switch, MAC address, and locator IP.
- `add-mcast-remote <ls_name> <dst_ip> <locator_ip>`: Add a multicast remote entry for the specified logical switch, destination IP, and locator IP.

The function should return a dictionary containing the resulting state of the VTEP, including:
- Logical switches and their associated VXLAN IDs.
- Virtual machines and their bindings to logical switches with VLAN IDs.
- Unicast and multicast remote connections for each logical switch.

Assume that the input commands are well-formed and that there are no conflicting or invalid configurations.
"""

from typing import List, Dict, Any

def simulate_vtep_config(commands: List[str]) -> Dict[str, Any]:
    vtep_state = {
        "logical_switches": {},
        "vm_bindings": {},
        "unicast_remotes": {},
        "multicast_remotes": {}
    }

    for command in commands:
        tokens = command.split()
        if tokens[0] == "add-ls":
            ls_name = tokens[1]
            vtep_state["logical_switches"][ls_name] = None
        elif tokens[0] == "set" and tokens[1] == "Logical_Switch":
            ls_name = tokens[2]
            vxlan_id = int(tokens[3].split("=")[1])
            vtep_state["logical_switches"][ls_name] = vxlan_id
        elif tokens[0] == "bind-ls":
            bridge_name, vm_name, vlan_id, ls_name = tokens[1:]
            vtep_state["vm_bindings"][vm_name] = {
                "ls_name": ls_name,
                "vlan_id": int(vlan_id)
            }
        elif tokens[0] == "add-ucast-remote":
            ls_name, mac_address, locator_ip = tokens[1:]
            if ls_name not in vtep_state["unicast_remotes"]:
                vtep_state["unicast_remotes"][ls_name] = {}
            vtep_state["unicast_remotes"][ls_name][mac_address] = locator_ip
        elif tokens[0] == "add-mcast-remote":
            ls_name, dst_ip, locator_ip = tokens[1:]
            if ls_name not in vtep_state["multicast_remotes"]:
                vtep_state["multicast_remotes"][ls_name] = {}
            vtep_state["multicast_remotes"][ls_name][dst_ip] = locator_ip

    return vtep_state
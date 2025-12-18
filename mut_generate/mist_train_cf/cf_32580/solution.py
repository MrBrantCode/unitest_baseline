"""
QUESTION:
Write a function `generate_nmcli_commands` that takes a list of network configurations as input and produces the corresponding `nmcli` commands for configuring the OVS interfaces and ports. Each network configuration is a dictionary containing the details of the connection interface, type, slave type, master bridge name, VLAN tag, connection name, and IPv4 configuration details. 

The function should return a list of `nmcli` commands, one for each network configuration. The `nmcli` command should be in the format "nmcli c add type <connection type> <key> <value>" where `<connection type>` is the type of the connection and `<key> <value>` are the key-value pairs from the network configuration dictionary. The `type` key from the dictionary should be excluded from the key-value pairs in the `nmcli` command.

The function should handle network configurations with varying numbers of key-value pairs and should not assume any specific order of the key-value pairs in the dictionary. The function should also handle the case where a key-value pair has a value of `None` or an empty string.
"""

def generate_nmcli_commands(network_configurations):
    nmcli_commands = []
    for config in network_configurations:
        command = "nmcli c add type {} ".format(config["type"])
        for key, value in config.items():
            if key != "type" and value not in [None, ""]:
                command += "{} {} ".format(key, value)
        nmcli_commands.append(command.strip())
    return nmcli_commands
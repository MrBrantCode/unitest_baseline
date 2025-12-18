"""
QUESTION:
Implement a method `_resolve_node` that resolves a node based on its name within a given dictionary data structure. The data structure is a dictionary with a "nodes" key containing another dictionary with node names as keys. The method takes a node name as a string and returns the key of the node within the "nodes" dictionary by matching the last part of the node name with the keys in the "nodes" dictionary. If a match is found, return the corresponding key; otherwise, return `None`. The node name can be in the format "subnode" or "node.subnode".
"""

from typing import Optional, Dict

def resolve_node(definition: Dict, name: str) -> Optional[str]:
    """
    Resolves a node based on its name within a given dictionary data structure.

    Args:
    definition (Dict): A dictionary with a "nodes" key containing another dictionary with node names as keys.
    name (str): A node name as a string.

    Returns:
    Optional[str]: The key of the node within the "nodes" dictionary if a match is found; otherwise, None.
    """
    key = next((k for k in definition["nodes"].keys() if name == k.split(".")[-1]), None)
    return key
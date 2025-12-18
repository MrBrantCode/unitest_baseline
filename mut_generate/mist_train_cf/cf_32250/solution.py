"""
QUESTION:
Implement the function `process_nodes(nodes, stop_on_next, tagid_required)` to filter a list of XML nodes based on the given conditions. The function takes a list of XML nodes, where each node has `tag_type` and `attributes`, and two boolean flags `stop_on_next` and `tagid_required`. The function should return a filtered list of nodes. 

If `stop_on_next` is `True` and `tagid_required` is `True`, return nodes where the `attributes` contain a key named `TAGID`. If `stop_on_next` is `True` and `tagid_required` is `False`, return nodes where the `tag_type` is `UNPAIRED_TAG`.
"""

from typing import List

class Node:
    def __init__(self, tag_type, attributes):
        self.tag_type = tag_type
        self.attributes = attributes

def process_nodes(nodes: List[Node], stop_on_next: bool, tagid_required: bool) -> List[Node]:
    filtered_nodes = []
    for node in nodes:
        if stop_on_next:
            if (tagid_required and 'TAGID' in node.attributes) or (not tagid_required and node.tag_type == 'UNPAIRED_TAG'):
                filtered_nodes.append(node)
    return filtered_nodes
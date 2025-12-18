"""
QUESTION:
Implement a function `filter_selected_node` that filters a tree-like data structure to show information for the selected node only. The tree is represented as a list of dictionaries, where each dictionary represents a node with "id", "name", and "children" keys.

The function takes in the tree data structure and the ID of the selected node, and returns a new tree structure containing information only for the selected node and its descendants. If the selected node is not found in the tree, the function should return an empty list.
"""

from typing import List, Dict, Union

def filter_selected_node(tree: List[Dict[str, Union[int, str, List]]], selected_id: int) -> List[Dict[str, Union[int, str, List]]]:
    """
    Filters a tree-like data structure to show information for the selected node only.

    Args:
        tree (List[Dict[str, Union[int, str, List]]]): The tree data structure.
        selected_id (int): The ID of the selected node.

    Returns:
        List[Dict[str, Union[int, str, List]]]: A new tree structure containing information only for the selected node and its descendants.
    """
    def find_node(node, selected_id):
        if node["id"] == selected_id:
            return node
        for child in node.get("children", []):
            result = find_node(child, selected_id)
            if result:
                return result
        return None

    selected_node = next((find_node(node, selected_id) for node in tree if find_node(node, selected_id)), None)
    return [selected_node] if selected_node else []
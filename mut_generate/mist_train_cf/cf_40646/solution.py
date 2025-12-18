"""
QUESTION:
Implement a `parse_tree` function that takes a list of API endpoint patterns and a dictionary tree as input. The function should recursively parse the patterns and populate the tree with a nested dictionary structure representing the API endpoints.

The patterns list contains strings where each string represents an API endpoint pattern, and the tree should be a dictionary where keys represent parts of the endpoint patterns and values represent sub-endpoints or leaf endpoints. The function should handle cases where endpoint patterns share common prefixes and construct the tree accordingly.

The function should return the populated tree. Assume the input patterns are valid and do not contain empty strings or trailing slashes.
"""

from collections import defaultdict

def parse_tree(patterns, tree):
    """
    Recursively parse the patterns and populate the tree with a nested dictionary structure representing the API endpoints.

    Args:
    patterns (list): A list of API endpoint patterns.
    tree (dict): A dictionary tree to be populated.

    Returns:
    dict: The populated tree.
    """
    for pattern in patterns:
        parts = pattern.split('/')
        current_tree = tree
        for part in parts:
            if part not in current_tree:
                current_tree[part] = defaultdict(dict)
            current_tree = current_tree[part]
    return tree
"""
QUESTION:
Create a function `validate_node_name` that takes a string `node_name` as input and checks if it contains only the characters 0-9, a-z, A-Z, underscore (_), and hyphen (-), and is not empty. If the `node_name` is valid, the function should return "Valid Node name"; otherwise, it should return "Invalid Node name".
"""

import re

def validate_node_name(node_name):
    pattern = r'^[0-9a-zA-Z_-]+$'
    if re.match(pattern, node_name):
        return "Valid Node name"
    else:
        return "Invalid Node name"
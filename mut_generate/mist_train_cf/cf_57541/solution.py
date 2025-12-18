"""
QUESTION:
Write a function `xml_to_nested_list(xml_string)` that takes a string of XML data as input, parses it, and returns a nested list representing the XML node tree, preserving the hierarchy of the nodes. The function should handle cases of malformed XML, raise an error, and print an error message. If a node has duplicate children with the same tag, print a warning message but include both children in the list.
"""

import xml.etree.ElementTree as ET

def xml_to_nested_list(xml_string):
    try:
        # Parse XML string
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        print("Malformed XML detected. Aborting.")
        return None

    def parse_node(node):
        # Initialize list with node tag
        nested_list = [node.tag]

        # Initialize set for duplicate detection
        node_set = set()

        # Iterate over child nodes
        for child in node:
            # Warn if duplicate moniker
            if child.tag in node_set:
                print(f"Warning: Duplicate moniker '{child.tag}' in same parent node '{node.tag}'")
            node_set.add(child.tag)

            # Recursively parse child nodes
            nested_list.append(parse_node(child))

        return nested_list

    return parse_node(root)
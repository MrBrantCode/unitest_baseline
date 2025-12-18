"""
QUESTION:
Write a function named `parse_xml` that takes the path to an XML file as input and returns a list of all node names in the XML document in the order they appear. The function should use the xml.etree.ElementTree module to parse the XML file.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_file_path):
    """
    Parses an XML file and returns sequential list of node names
    """
    # Parse XML with ElementTree
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # List to hold node names
    node_names = []

    # Recursive function to visit all nodes of the tree
    def visit_node(node):
        # Add current node name to the list
        node_names.append(node.tag)

        # Recursion
        for child in node:
            visit_node(child)

    # Start visiting from root node
    visit_node(root)

    return node_names
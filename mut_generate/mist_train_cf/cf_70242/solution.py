"""
QUESTION:
Create a function `extract_node_names(xml_string, namespace=None)` that takes a string representing an XML document and an optional namespace string. The function should return a list of all node names in the XML document, filtered by the specified namespace if provided.
"""

import xml.etree.ElementTree as ET

def extract_node_names(xml_string, namespace=None):
    tree = ET.ElementTree(ET.fromstring(xml_string))
    node_names = []

    for elem in tree.iter():
        # If a namespace is requested, skip elements not in that namespace
        if namespace and not elem.tag.startswith(f'{{{namespace}}}'):
            continue
        # Get node name, ignoring namespace part
        node_name = elem.tag.split('}')[-1]
        node_names.append(node_name)

    return node_names
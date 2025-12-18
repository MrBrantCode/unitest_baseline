"""
QUESTION:
Implement a function called `xml_to_dict` that transforms a given XML element into its equivalent dictionary representation, preserving the hierarchical data structure. The function should recursively process the XML elements and their children. Assume that the XML does not have attributes on the tags and that the tags do not repeat inside a parent tag.
"""

import xml.etree.ElementTree as ET

def xml_to_dict(root):
    """
    Transform an XML element into its equivalent dictionary representation.

    Args:
    root: The root XML element to transform.

    Returns:
    A dictionary representing the XML element's hierarchical data structure.
    """
    d = {}
    for child in root:
        if len(child) > 0:
            d[child.tag] = xml_to_dict(child)
        else:
            d[child.tag] = child.text
    return d
"""
QUESTION:
Write a function named `get_child_elements` that takes an XML string or the root of an XML element tree as input, and returns a list of text values of all 'child' elements nested within the 'parent' elements. The function should use the 'ElementTree' module to parse the XML data.
"""

import xml.etree.ElementTree as ET

def get_child_elements(root):
    """
    Extracts text values of 'child' elements within 'parent' elements in an XML tree.

    Args:
    root (ET.Element): The root element of the XML tree.

    Returns:
    list: A list of text values of 'child' elements.
    """
    return [child.text for child in root.findall('child')]
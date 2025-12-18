"""
QUESTION:
Design a function named `xml_to_dict` that takes an XML element as input, and returns a dictionary representation of the XML element. The function should handle nested elements by recursively calling itself and handle missing or null entries by returning `None` as the value. If an element has multiple children with the same tag, the function should store them in a list.
"""

import xml.etree.ElementTree as ET

def xml_to_dict(element):
    """
    Converts an XML element into a dictionary.

    Args:
    element (xml.etree.ElementTree.Element): The XML element to be converted.

    Returns:
    dict: A dictionary representation of the XML element.
    """
    if len(element) == 0:
        return element.text
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in result:
            if type(result[child.tag]) is list:
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result
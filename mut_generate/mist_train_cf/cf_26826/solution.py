"""
QUESTION:
Write a `convert` function within the `SubstanceCVConverter` class that takes an XML element `xml` as input. The function should return a dictionary containing all attributes from `xml` and its nested elements. The dictionary keys should be the attribute names for the top-level attributes, and for nested elements, the key should be the element tag with a list of dictionaries as the value, where each dictionary represents the attributes of a nested element.
"""

def convert(xml):
    item = xml.attrib
    # Handle nested XML elements
    for child in xml:
        if child.tag not in item:
            item[child.tag] = []
        item[child.tag].append(convert(child))
    return item
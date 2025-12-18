"""
QUESTION:
Write a function `find_elements_with_given_id(xml_string, id_attr)` that takes an XML string and an ID attribute value as input, and returns a list of elements with the given ID attribute. The function should have a time complexity of O(n), where n is the number of elements in the XML document, and should correctly handle nested elements.
"""

import xml.etree.ElementTree as ET

def find_elements_with_given_id(xml_string, id_attr):
    root = ET.fromstring(xml_string)
    result = []

    def find_elements_with_id(root):
        if 'id' in root.attrib and root.attrib['id'] == id_attr:
            result.append(root)
        for child in root:
            find_elements_with_id(child)

    find_elements_with_id(root)
    return result
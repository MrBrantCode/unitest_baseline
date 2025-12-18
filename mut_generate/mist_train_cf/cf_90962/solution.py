"""
QUESTION:
Write a function `dict_to_xml` that takes a dictionary as input and generates an XML format to store the information. The dictionary can contain nested dictionaries and lists. The function should have a time complexity of O(n), where n is the total number of key-value pairs in the input dictionary, and a space complexity of O(n), where n is the total number of key-value pairs in the input dictionary.
"""

import xml.etree.ElementTree as ET

def dict_to_xml(data, root_name="data"):
    root = ET.Element(root_name)
    dict_to_xml_rec(data, root)
    return ET.tostring(root).decode()

def dict_to_xml_rec(data, root):
    for key, value in data.items():
        if isinstance(value, dict):
            sub_element = ET.SubElement(root, key)
            dict_to_xml_rec(value, sub_element)
        elif isinstance(value, list):
            for item in value:
                sub_element = ET.SubElement(root, key)
                dict_to_xml_rec(item, sub_element)
        else:
            element = ET.SubElement(root, key)
            element.text = str(value)
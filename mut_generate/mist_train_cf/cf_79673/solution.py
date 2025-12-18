"""
QUESTION:
Create a function `xml_to_dict` that converts an XML structure into a nested dictionary, where each 'parent' element becomes a key with a value of another dictionary. 'Child' elements should also become keys in these nested dictionaries, pointing to their own dictionaries of children, if they have any. The function should be able to handle an arbitrary degree of nesting. 

Restrictions: the function should be implemented in Python using the xml.etree.ElementTree module, and should not handle XML attributes or namespaces.
"""

import xml.etree.ElementTree as ET

def xml_to_dict(element):
    if len(element) == 0: 
        return element.text 
    return {child.tag: xml_to_dict(child) for child in element}

def xml_to_dict_main(xml_data):
    root = ET.XML(xml_data)
    return {root.tag: xml_to_dict(root)}
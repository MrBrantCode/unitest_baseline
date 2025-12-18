"""
QUESTION:
Write a function `xml_to_dict(xml_string)` that takes a string representation of an XML data structure as input and returns the XML data structure translated into a Python dictionary. The function should be able to handle nested XML structures and report any XML parsing errors. It should also be scalable to accommodate additional tags and attributes.
"""

import xml.etree.ElementTree as ET

def xml_to_dict(xml_string):
    try:
        root = ET.fromstring(xml_string)
        result_dict = {}
        
        for child in root:
            if len(child) == 0:
                result_dict[child.tag] = child.text
            else:
                nested_dict = {}
                for nested_child in child:
                    if len(nested_child) == 0:
                        nested_dict[nested_child.tag] = nested_child.text
                    else:
                        nested_dict[nested_child.tag] = xml_to_dict(ET.tostring(nested_child, encoding='unicode'))
                result_dict[child.tag] = nested_dict
        return result_dict
    except ET.ParseError:
        return 'Invalid XML structure'
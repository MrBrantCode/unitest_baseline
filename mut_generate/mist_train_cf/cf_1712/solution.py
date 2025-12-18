"""
QUESTION:
Write a function `json_to_xml(json_string)` that takes a JSON string as input and returns its equivalent XML string. The function should handle any valid JSON input, including complex nested structures and large data sets, and wrap the XML output in a 'root' element.
"""

import json
import xml.etree.ElementTree as ET

def json_to_xml(json_string):
    def parse_element(element, parent):
        if isinstance(element, dict):
            for key, value in element.items():
                if isinstance(value, list):
                    for item in value:
                        child = ET.SubElement(parent, key)
                        parse_element(item, child)
                else:
                    child = ET.SubElement(parent, key)
                    parse_element(value, child)
        elif isinstance(element, list):
            for item in element:
                parse_element(item, parent)
        else:
            parent.text = str(element)

    data = json.loads(json_string)
    root = ET.Element('root')
    parse_element(data, root)
    xml_string = ET.tostring(root, encoding='utf-8', method='xml')
    return xml_string.decode('utf-8')
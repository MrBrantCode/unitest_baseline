"""
QUESTION:
Write a function `convert_xml_to_json(xml_string)` that takes an XML string as input and returns a JSON string. The function should maintain the original hierarchical structure of the XML elements and only include XML elements that have an attribute `filter` set to `"true"`. If an XML element does not have children, its text content should be included in the JSON output.
"""

import xml.etree.ElementTree as ET
import json

def convert_xml_to_json(xml_string):
    xml_root = ET.fromstring(xml_string)
    
    def convert_element(element):
        json_obj = {'tag': element.tag}
        
        if len(element) > 0:
            json_obj['children'] = [convert_element(child) for child in element if child.attrib.get('filter', '') == 'true']
        else:
            json_obj['text'] = element.text.strip() if element.text else ''
        
        return json_obj
    
    return json.dumps(convert_element(xml_root), indent=4)
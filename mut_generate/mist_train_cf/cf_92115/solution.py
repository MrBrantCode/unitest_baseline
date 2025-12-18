"""
QUESTION:
Write a function `convert_xml_to_json(xml_string)` that converts an XML string into a JSON object while maintaining the original hierarchical structure of the XML elements. The JSON output should only include XML elements with a 'filter' attribute set to 'true'.
"""

import xml.etree.ElementTree as ET
import json

def filter_elements(xml_element):
    # Add your criteria for filtering specific XML elements
    return xml_element.attrib.get('filter', '') == 'true'

def convert_xml_to_json(xml_string):
    xml_root = ET.fromstring(xml_string)
    
    def convert_element(element):
        json_obj = {'tag': element.tag}
        
        if len(element) > 0:
            json_obj['children'] = [convert_element(child) for child in element if filter_elements(child)]
        else:
            json_obj['text'] = element.text.strip() if element.text else ''
        
        return json_obj
    
    return json.dumps(convert_element(xml_root), indent=4)
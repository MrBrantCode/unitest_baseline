"""
QUESTION:
Create a function `xml_to_json(xml_str)` that takes a string `xml_str` containing XML data as input and returns a JSON string. The function should convert the given XML data into JSON format, where the XML data is in the format `<staff><employee>...</employee></staff>`. The XML data contains employee information, including `id`, `name`, `positions`, and `contact` details. The function should use `xml.etree.ElementTree` for XML parsing and `json` for JSON conversion. The output JSON string should be in the format of a dictionary where the key is the employee `id` and the value is another dictionary containing the employee details.
"""

import xml.etree.ElementTree as ET
import json

def xml_to_json(xml_str):
    data = dict()
    root = ET.fromstring(xml_str)
    for employee in root.findall('employee'):
        id = employee.find('id').text
        data[id] = {}
        data[id]['name'] = employee.find('name').text
        positions = employee.find('positions')
        data[id]['positions'] = {
            'title': positions.find('title').text,
            'department': positions.find('department').text,
        }
        contact = employee.find('contact')
        data[id]['contact'] = {
            'email': contact.find('email').text,
            'phone': contact.find('phone').text
        }
    
    return json.dumps(data)
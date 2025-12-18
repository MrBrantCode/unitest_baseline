"""
QUESTION:
Write a function named `convert_xml_to_json` that takes an XML file path as input, converts the XML data to JSON, and returns the JSON string. The function should reorder the JSON keys based on the length of their values in a hierarchy and sort the records alphabetically by the "name" attribute. The 'address' element in the XML should be abstracted into 'street_address' in the JSON output. Assume all records have the 'name' and 'age' attributes and an 'address' child.
"""

import xml.etree.ElementTree as ET
import json

def convert_xml_to_json(xml_file_path):
    """
    This function takes an XML file path as input, converts the XML data to JSON, 
    and returns the JSON string. The function reorders the JSON keys based on the 
    length of their values in a hierarchy and sorts the records alphabetically by 
    the "name" attribute. The 'address' element in the XML is abstracted into 
    'street_address' in the JSON output.
    """
    
    # Parse XML using ElementTree
    xml_root = ET.parse(xml_file_path).getroot()
    
    # Prepare the data for JSON
    data = {}
    data['records'] = []
    
    for record in xml_root.findall('.//record'):
        name = record.attrib['name']
        age = record.attrib['age']
        street_address = record.find('address').text
        data['records'].append({
            "name": name,
            "age": age,
            "street_address": street_address
        })
    
    # Sort records based on the "name" and ordering by the length of their values
    data['records'] = sorted(data['records'], key = lambda i : (len(i['name']) + len(i['age']) + len(i['street_address']), i['name']))
    
    # Convert list to json
    json_object = json.dumps(data, indent = 4)
    
    return json_object
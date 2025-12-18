"""
QUESTION:
Create a function `process_op_commands(xml_output)` that takes XML output as input, parses it to extract specific fields, and returns a list of dictionaries containing the extracted information. The function should iterate through the XML elements to extract the fields, with each dictionary in the list representing a single entry of extracted information. The XML output has a specific structure with elements that contain attributes and values to be extracted.
"""

from xml.etree import ElementTree

def process_op_commands(xml_output):
    root = ElementTree.fromstring(xml_output)
    extracted_info = []

    for entry in root.findall('.//entry'):
        extracted_data = {
            'field1': entry.find('field1').text,
            'field2': entry.find('field2').text,
            # Add more fields as needed
        }
        extracted_info.append(extracted_data)

    return extracted_info
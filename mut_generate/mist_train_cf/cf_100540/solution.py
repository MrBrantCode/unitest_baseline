"""
QUESTION:
Write a function named `correct_sentence` that takes an XML string as input, updates the text content of the 'subject' and 'object' elements, and returns the updated XML string. The function should use the `xml.etree.ElementTree` module for parsing and serializing the XML data.
"""

import xml.etree.ElementTree as ET

def correct_sentence(xml_str):
    # Parse the XML data
    root = ET.fromstring(xml_str)

    # Traverse the XML tree to locate the subject and object elements
    subject_elem = root.find('subject')
    object_elem = root.find('object')

    # Update the text content of the subject and object elements with the corrected values
    subject_elem.text = 'He'
    object_elem.text = 'her'

    # Serialize the updated XML tree back into a string
    updated_xml_str = ET.tostring(root, encoding='unicode')

    return updated_xml_str
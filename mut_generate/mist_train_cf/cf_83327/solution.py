"""
QUESTION:
Create a function named `parse_student_xml` that takes a string `xml_data` representing an XML document. The function should parse the XML data, extract the characteristics of the 'student' label and its nested labels, and count the total number of each unique characteristic. If the provided XML data does not conform to the XML standard, the function should raise an exception.
"""

import xml.etree.ElementTree as ET

def parse_student_xml(xml_data):
    """
    Parse the XML data, extract the characteristics of the 'student' label and its nested labels,
    and count the total number of each unique characteristic.

    Args:
    xml_data (str): A string representing an XML document.

    Returns:
    dict: A dictionary containing the total number of each unique characteristic.

    Raises:
    ET.ParseError: If the provided XML data does not conform to the XML standard.
    """

    # Parse the XML data
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError:
        raise

    # Initialize a dictionary to count the characteristics
    char_count = {}

    # Explore the 'student' label and any nested labels
    for elem in root.iter():
        for key, value in elem.attrib.items():
            char_count[key] = char_count.get(key, 0) + 1

    return char_count
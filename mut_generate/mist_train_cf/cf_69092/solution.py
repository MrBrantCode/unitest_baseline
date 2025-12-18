"""
QUESTION:
Write a Python function named `parse_xml` to parse an XML file using the xml.etree.ElementTree module. The function should take the XML file name as a string and return the root element of the XML document. The function should also include a basic error handling mechanism to catch and print any exceptions that occur during the parsing process.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    """
    Parse an XML file and return the root element.

    Args:
    xml_file (str): The name of the XML file to parse.

    Returns:
    The root element of the XML document.

    Raises:
    Exception: If any error occurs during parsing.
    """
    try:
        tree = ET.parse(xml_file)
        return tree.getroot()
    except Exception as e:
        print(f"Error parsing XML file: {e}")
        return None
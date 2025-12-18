"""
QUESTION:
Write a function `parse_xml(xml_string)` that takes a string of XML data as input, parses it, and prints the tag names and their corresponding values. The function should handle cases where the XML string is invalid, required tags are missing, or the tag values do not match a specified data type. The function should also handle nested tags and attributes, printing the tag hierarchy and attribute names and values. If the XML string is invalid, the function should print an error message.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    """
    Parse an XML string, printing the tag names and their corresponding values.
    
    Args:
    xml_string (str): The XML string to parse.
    """
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print("Invalid XML:", e)
        return

    def parse_element(element, indent=""):
        """
        Recursively parse an XML element and its children.
        
        Args:
        element (ET.Element): The XML element to parse.
        indent (str, optional): The indentation to use for printing. Defaults to "".
        """
        print(f"{indent}- Tag name: {element.tag}, Value: {element.text}")
        for child in element:
            parse_element(child, indent + "  ")
        for attribute, value in element.attrib.items():
            print(f"{indent}  Attribute: {attribute}, Value: {value}")
    
    parse_element(root)
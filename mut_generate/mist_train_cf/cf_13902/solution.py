"""
QUESTION:
Write a function `parse_xml_string(xml_string)` that takes a string representing an XML document as input, parses the string, and prints the tag names and their corresponding values. The function should handle cases where the input string is an invalid XML.
"""

import xml.etree.ElementTree as ET

def parse_xml_string(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        print("Invalid XML string")
        return

    for element in root.iter():
        print(f"- Tag name: {element.tag}, Value: {element.text}")
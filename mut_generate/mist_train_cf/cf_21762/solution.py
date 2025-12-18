"""
QUESTION:
Implement a function `parse_xml(xml_string)` to parse a given XML string, print the tag names and their corresponding values, and handle cases where the XML string is invalid, a required tag is missing, or the tag values do not match a specified data type. The function should validate that the XML string is well-formed, contains only valid tags and attributes, and handle cases where the XML string contains nested tags and attributes.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        print("Invalid XML:", e)
        return

    def parse_element(element, indent=""):
        print(f"{indent}- Tag name: {element.tag}, Value: {element.text}")
        for child in element:
            parse_element(child, indent + "  ")
        for attribute, value in element.attrib.items():
            print(f"{indent}  Attribute: {attribute}, Value: {value}")

    parse_element(root)
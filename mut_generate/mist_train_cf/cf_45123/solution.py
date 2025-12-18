"""
QUESTION:
Implement a function named `verify_and_print` that takes a string representing an XML structure as input and returns a message indicating whether the XML is valid or not. The function should also print the constituent element identifiers and their child elements, indented to show their nesting levels. If the XML string is not properly nested or has missing tags, the function should return "Invalid XML: Not properly nested or missing tags".
"""

import xml.etree.ElementTree as ET

def verify_and_print(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        return "Invalid XML: Not properly nested or missing tags"
    else:
        def traverse(root, depth=0):
            print('-' * depth + root.tag)
            for child in root:
                traverse(child, depth=depth + 1)
        traverse(root)
        return "Valid XML"
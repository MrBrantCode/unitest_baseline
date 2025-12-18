"""
QUESTION:
Write a function `parse_xml(xml_string)` that takes an XML string as input and returns a dictionary representing the hierarchical structure of the XML document. The function should handle nested elements and attributes, and support both opening and self-closing tags. The time complexity should be O(n), where n is the number of elements in the XML document, and the space complexity should be O(m), where m is the maximum depth of nested elements.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    return parse_element(root)

def parse_element(element):
    result = {}
    result.update(element.attrib)

    for child in element:
        child_data = parse_element(child)
        if child.tag in result:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_data)
        else:
            result[child.tag] = child_data

    if element.text:
        result['text'] = element.text.strip()

    return result
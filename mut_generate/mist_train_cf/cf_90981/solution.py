"""
QUESTION:
Write a function `parse_xml(xml_string)` to convert an XML document to a dictionary. The function should handle nested elements and attributes, support both opening and self-closing tags, and maintain the hierarchical structure of the XML document. It should also properly escape special characters. The time complexity should be O(n), where n is the number of elements in the XML document, and the space complexity should be O(m), where m is the maximum depth of nested elements.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    return _parse_element(root)

def _parse_element(element):
    result = {}
    # Process attributes
    result.update(element.attrib)

    # Process child elements
    for child in element:
        child_data = _parse_element(child)
        if child.tag in result:
            # If the tag already exists in the result, convert it to a list
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_data)
        else:
            result[child.tag] = child_data

    # Process text content
    if element.text:
        result['text'] = element.text.strip()

    return result
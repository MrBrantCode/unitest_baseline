"""
QUESTION:
Write a function called `xmlToJson` that takes an XML element as input and returns a JSON object representing the element, including its tag, attributes, text, and children, while maintaining the hierarchical relationships present in the original XML. The function should be able to handle edge cases such as self-closing tags, nested tags, and multiple attributes, and should not be limited to a specific XML structure.
"""

import json
import xml.etree.ElementTree as ET

def xmlToJson(element):
    node = {}

    text = getattr(element, 'text', None)
    if text is not None:
        node['text'] = text.strip()

    attributes = element.attrib
    if attributes:
        node['attributes'] = attributes

    children = list(element)
    if children:
        node['children'] = [xmlToJson(child) for child in children]

    return {element.tag: node}
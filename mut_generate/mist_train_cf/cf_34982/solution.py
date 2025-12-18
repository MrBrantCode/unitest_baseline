"""
QUESTION:
Write a function named `count_svg_attributes` that takes a string `svg_code` as input and returns a dictionary containing the counts of each attribute within the `<g>` tag in the given SVG code. The function should be case-sensitive and only consider attributes within the `<g>` tag.
"""

import xml.etree.ElementTree as ET

def count_svg_attributes(svg_code: str) -> dict:
    attribute_counts = {}
    root = ET.fromstring(svg_code)
    g_tag = root.find('g')
    if g_tag is not None:
        for element in g_tag:
            for attribute in element.attrib:
                if attribute in attribute_counts:
                    attribute_counts[attribute] += 1
                else:
                    attribute_counts[attribute] = 1
    return attribute_counts
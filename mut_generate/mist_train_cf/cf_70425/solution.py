"""
QUESTION:
Write a function named `break_svg_into_individual_parts` that takes an SVG string as input and returns a list of strings, each representing an individual `<path>` element from the SVG data. The function should use Python's `xml.etree.ElementTree` library to parse the SVG. The SVG data may contain a namespace, which should be handled correctly by the function.
"""

import xml.etree.ElementTree as ET

def break_svg_into_individual_parts(svg_data):
    root = ET.fromstring(svg_data)
    individual_parts = []
    for path in root.findall('.//{http://www.w3.org/2000/svg}path'):
        individual_parts.append(ET.tostring(path, encoding='unicode'))
    return individual_parts
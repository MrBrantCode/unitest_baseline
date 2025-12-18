"""
QUESTION:
Implement a function `extractRectangles(svg)` that takes a string `svg` representing a well-formed SVG file as input. The function should return a list of dictionaries, where each dictionary contains the following information about a rectangle defined by a `<rect>` tag in the SVG file: `x`, `y`, `width`, `height`, `rx` (default 0 if not specified), and `ry` (default 0 if not specified). The attributes in the `<rect>` tags may appear in any order.
"""

import xml.etree.ElementTree as ET

def extractRectangles(svg):
    root = ET.fromstring(svg)
    rectangles = []
    for rect in root.findall('.//rect'):
        x = float(rect.get('x', 0))
        y = float(rect.get('y', 0))
        width = float(rect.get('width'))
        height = float(rect.get('height'))
        rx = float(rect.get('rx', 0))
        ry = float(rect.get('ry', 0))
        rectangles.append({'x': x, 'y': y, 'width': width, 'height': height, 'rx': rx, 'ry': ry})
    return rectangles
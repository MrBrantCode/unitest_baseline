"""
QUESTION:
Create a function `age_svg` that takes in an SVG image as a string, applies effects to give it a weathered and aged appearance, and returns the modified SVG image. The function should change the colors to more muted or earth tones, add noise or texture, introduce transparency or opacity, and simulate rough edges.
"""

import xml.etree.ElementTree as ET
from io import StringIO

def age_svg(svg_image):
    # Parse the SVG
    tree = ET.parse(StringIO(svg_image))
    root = tree.getroot()

    # Define a filter to add texture
    filter_element = ET.Element('filter', attrib={
        'id': 'age-filter',
        'x': '0',
        'y': '0',
        'width': '100%',
        'height': '100%',
        'filterUnits': 'objectBoundingBox'
    })

    fe_turbulence = ET.SubElement(filter_element, 'feTurbulence', attrib={
        'type': 'fractalNoise',
        'baseFrequency': '0.02',
        'numOctaves': '4',
        'seed': '12345',
        'result': 'wavy'
    })

    fe_displacement_map = ET.SubElement(filter_element, 'feDisplacementMap', attrib={
        'in': 'SourceGraphic',
        'in2': 'wavy',
        'scale': '10',
        'xChannelSelector': 'R',
        'yChannelSelector': 'G'
    })

    root.append(filter_element)

    # Apply the filter to the SVG
    for element in root.iter():
        if element.tag.endswith('path') or element.tag.endswith('rect'):
            element.set('filter', 'url(#age-filter)')

            # Change the colors to more muted or earth tones
            if 'fill' in element.attrib:
                element.set('fill', '#964B00')  # Replace with desired earth tone color

            # Add transparency or opacity
            if 'opacity' not in element.attrib:
                element.set('opacity', '0.8')  # Replace with desired opacity

    # Return the modified SVG
    io = StringIO()
    tree.write(io, encoding='unicode')
    return io.getvalue()
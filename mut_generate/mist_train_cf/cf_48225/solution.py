"""
QUESTION:
Create a function called `weathered_svg` that takes an SVG file as input and returns a weathered version of the SVG. The function should use SVG/CSS to achieve the weathered effect, without converting the SVG to a raster format.
"""

import xml.etree.ElementTree as ET

def weathered_svg(svg_file):
    """
    This function takes an SVG file as input and returns a weathered version of the SVG.
    
    Args:
    svg_file (str): The input SVG file path.
    
    Returns:
    str: The weathered SVG as a string.
    """
    
    # Parse the SVG file using ElementTree
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # Add a filter to the SVG
    filter_elem = ET.SubElement(root, 'filter')
    filter_elem.set('id', 'weathered')
    filter_elem.set('x', '-10%')
    filter_elem.set('y', '-10%')
    filter_elem.set('width', '120%')
    filter_elem.set('height', '120%')
    
    # Use <feTurbulence> and <feDisplacementMap> in a <filter> element
    fe_turbulence = ET.SubElement(filter_elem, 'feTurbulence')
    fe_turbulence.set('type', 'fractalNoise')
    fe_turbulence.set('baseFrequency', '0.1')
    fe_turbulence.set('numOctaves', '2')
    fe_turbulence.set('seed', '1')
    
    fe_displacement_map = ET.SubElement(filter_elem, 'feDisplacementMap')
    fe_displacement_map.set('in', 'SourceGraphic')
    fe_displacement_map.set('in2', 'turbulence')
    fe_displacement_map.set('scale', '10')
    fe_displacement_map.set('xChannelSelector', 'R')
    fe_displacement_map.set('yChannelSelector', 'G')
    
    # Use <feColorMatrix> in a <filter> to desaturate colors
    fe_color_matrix = ET.SubElement(filter_elem, 'feColorMatrix')
    fe_color_matrix.set('type', 'matrix')
    fe_color_matrix.set('values', '0.5 0.5 0.5 0 0 0.5 0.5 0.5 0 0 0.5 0.5 0.5 0 0 0 0 0 1 0')
    
    # Apply the filter to all elements in the SVG
    for elem in root.findall('.//'):
        if 'style' in elem.attrib:
            elem.set('style', elem.attrib['style'] + '; filter:url(#weathered)')
        else:
            elem.set('style', 'filter:url(#weathered)')
    
    # Return the weathered SVG as a string
    return ET.tostring(root, encoding='unicode')
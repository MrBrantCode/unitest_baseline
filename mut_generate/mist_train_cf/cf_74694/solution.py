"""
QUESTION:
Create a function called `flip_svg_horizontally` that takes an SVG string as input, adds the `transform="scale(-1,1)"` attribute to the SVG tag, and returns the modified SVG string. The function should work for any SVG string, regardless of its contents or attributes.
"""

def flip_svg_horizontally(svg_string):
    """
    This function flips an SVG image horizontally by adding the transform="scale(-1,1)" attribute to the SVG tag.
    
    Args:
        svg_string (str): The input SVG string.
    
    Returns:
        str: The modified SVG string with the horizontal flip transformation applied.
    """
    import xml.etree.ElementTree as ET
    
    # Parse the SVG string into an XML tree
    root = ET.fromstring(svg_string)
    
    # Add the transform attribute to the SVG tag
    root.attrib['transform'] = 'scale(-1,1)'
    
    # Convert the XML tree back to a string
    modified_svg_string = ET.tostring(root, encoding='unicode')
    
    return modified_svg_string
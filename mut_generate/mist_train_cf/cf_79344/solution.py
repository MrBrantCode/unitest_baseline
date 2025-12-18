"""
QUESTION:
Write a function `transform_to_xml` that takes a 3D matrix as input and returns its XML representation. The XML structure should consist of "item" elements for each 2D array, "subitem" elements for each 1D array inside the 2D array, and "element" elements for each value in the 1D array. Each element should have a unique "id" attribute for identification.
"""

import xml.etree.cElementTree as ET

def transform_to_xml(data):
    """
    This function transforms a 3D matrix into its XML representation.

    Args:
    data (list): A 3D matrix.

    Returns:
    xml.etree.ElementTree.Element: The root element of the XML structure.
    """

    # Create Root
    root = ET.Element("root")

    for i, two_dim in enumerate(data):
        item = ET.SubElement(root, "item")
        item.set("id", str(i+1))
        
        for j, one_dim in enumerate(two_dim):
            subitem = ET.SubElement(item, "subitem")
            subitem.set("id", str(j+1))
            
            for k, value in enumerate(one_dim):
                element = ET.SubElement(subitem, "element")
                element.set("id", str(k+1))
                element.text = str(value)
                
    return root
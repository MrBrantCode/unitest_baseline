"""
QUESTION:
Write a function `alter_xml_element` that takes an XML string and alters the numeric value of a specific element by combining (adding) the integer values of two other elements. The XML string should have the following structure: `<root> <element1>int</element1> <element2>int</element2> <element3>int</element3> </root>`. The function should return the modified XML string.
"""

import xml.etree.ElementTree as ET

def alter_xml_element(xml_string):
    """
    This function takes an XML string, alters the numeric value of a specific element 
    by adding the integer values of two other elements, and returns the modified XML string.

    Args:
    xml_string (str): The input XML string.

    Returns:
    str: The modified XML string.
    """
    
    # parse the XML document into an element tree
    root = ET.fromstring(xml_string)
    
    # find the elements we're interested in
    element1 = root.find('element1')
    element2 = root.find('element2')
    element3 = root.find('element3')
    
    # combine the values of element1 and element2 and alter the value of element3
    element3.text = str(int(element1.text) + int(element2.text))
    
    # return the modified XML document as a string
    return ET.tostring(root, encoding='unicode')
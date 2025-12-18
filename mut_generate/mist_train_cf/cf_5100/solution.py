"""
QUESTION:
Create a function `parse_xml` that takes an XML string as input and returns the value of the first attribute of the first element where the value of the "attr1" attribute is greater than 10, the value of the "attr2" attribute is less than 5, and the total number of attributes in the element is even.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    """
    This function takes an XML string as input, parses it, and returns the value of the first attribute 
    of the first element where the value of the "attr1" attribute is greater than 10, the value of the 
    "attr2" attribute is less than 5, and the total number of attributes in the element is even.
    
    Args:
        xml_string (str): The input XML string.
    
    Returns:
        str: The value of the first attribute of the first element that meets the conditions.
    """

    # Parse the XML string
    root = ET.fromstring(xml_string)

    # Find the first element that meets the conditions
    for element in root.findall('element'):
        # Check conditions
        if int(element.get('attr1')) > 10 and int(element.get('attr2')) < 5 and len(element.attrib) % 2 == 0:
            # Extract and return the value of the first attribute
            return list(element.attrib.values())[0]
    
    # If no element meets the conditions, return None
    return None
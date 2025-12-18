"""
QUESTION:
Write a Python function `find_elements_with_class` that takes an XML string as input and outputs the names of all elements with the "class" attribute. If the value of the "class" attribute contains the word "active", the function should also output the value of the "id" attribute.
"""

import xml.etree.ElementTree as ET

def find_elements_with_class(xml_data):
    """
    This function takes an XML string as input, parses it, and outputs the names of all elements with the "class" attribute.
    If the value of the "class" attribute contains the word "active", the function also outputs the value of the "id" attribute.

    Args:
        xml_data (str): The input XML string.

    Returns:
        list: A list containing the names of elements with the "class" attribute and the corresponding "id" values if the "class" attribute contains "active".
    """

    # Parse the XML document
    root = ET.fromstring(xml_data)

    # Find elements with the "class" attribute
    elements = root.findall('.//*[@class]')

    # Initialize an empty list to store the results
    result = []

    # Output names of elements with the "class" attribute
    for element in elements:
        # Append the element name to the result list
        result.append(element.tag)
        # Check if the "class" attribute value contains "active"
        if 'active' in element.get('class'):
            # Append the "id" value to the result list
            result.append(element.get('id'))

    return result
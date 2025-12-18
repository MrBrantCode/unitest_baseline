"""
QUESTION:
Create a function called `extract_data_points` that takes the path to an XML file and a condition as input. The function should parse the XML document, iterate over all `<item>` elements, and extract the text content if the specified attribute contains the given condition. The function should return a list of extracted data points.
"""

import xml.etree.ElementTree as ET

def extract_data_points(xml_path, condition, attribute_name):
    """
    Extracts data points from an XML file based on a given condition.

    Args:
    - xml_path (str): The path to the XML file.
    - condition (str): The condition to filter data points.
    - attribute_name (str): The name of the attribute to filter on.

    Returns:
    - list: A list of extracted data points.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    data_points = []
    for item in root.iter('item'):
        if condition in item.attrib.get(attribute_name, ''):
            data_points.append(item.text)
    
    return data_points
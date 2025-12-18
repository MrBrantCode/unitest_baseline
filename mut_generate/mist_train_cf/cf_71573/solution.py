"""
QUESTION:
Create a function named `deserialize_xml` that takes a string of XML data as input and returns the deserialized information. The XML data is in the format `<person><name>...</name><age>...</age><city>...</city></person>`. Use the `xml.etree.ElementTree` module in Python to parse the XML data and extract the `name`, `age`, and `city` information. The function should return a dictionary or a data structure that contains the extracted information.
"""

import xml.etree.ElementTree as ET

def deserialize_xml(xml_data):
    """
    Deserializes the given XML data and returns a dictionary containing the extracted information.
    
    Args:
        xml_data (str): The XML data to deserialize.
    
    Returns:
        dict: A dictionary containing the extracted information.
    """
    root = ET.fromstring(xml_data)
    return {
        'name': root.find('name').text,
        'age': root.find('age').text,
        'city': root.find('city').text
    }
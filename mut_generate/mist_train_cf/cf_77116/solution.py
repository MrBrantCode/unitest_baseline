"""
QUESTION:
Write a function named 'parse_and_manipulate_xml' using Python's ElementTree module to parse and manipulate XML data. This function should be able to read XML data from a string or a file, access elements, read data, modify data, add new elements, and remove elements. Ensure the function optimizes execution and accuracy while handling the XML data.
"""

import xml.etree.ElementTree as ET

def parse_and_manipulate_xml(file_name):
    """
    Parse and manipulate XML data from a file.

    Args:
    file_name (str): The name of the XML file to parse.

    Returns:
    The root element of the parsed XML data.
    """
    # Parse the XML file
    tree = ET.parse(file_name)
    root = tree.getroot()

    # Accessing the elements
    for elem in root:
        for subelem in elem:
            print(subelem.tag)

    # Reading the data
    print(root[0][1].text)

    # Modifying the XML data
    root[0][1].text = 'New data'

    # Adding new elements
    new_element = ET.SubElement(root[0], "new_element")
    new_element.text = "new data"

    # Removing an element
    root[0].remove(root[0][2])

    # Saving the changes
    tree.write(file_name)

    return root
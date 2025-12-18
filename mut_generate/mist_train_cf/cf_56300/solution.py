"""
QUESTION:
Create a function `parse_xml(xml_file)` that takes the path to an XML file as input. The function should parse the XML document, extract the labels of all compositional elements or nodes, sort them in ascending order, and return the sorted list of labels. The function should work with any XML file, regardless of its structure.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    """
    Parse the XML document, extract the labels of all compositional elements or nodes,
    sort them in ascending order, and return the sorted list of labels.

    Args:
        xml_file (str): The path to the XML file.

    Returns:
        list: A sorted list of labels.
    """
    # parse XML document
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # create list to store labels
    labels = []

    # function to find labels recursively
    def find_labels(element):
        # add current element's tag/label into the list
        labels.append(element.tag)
        # recursively explore all child elements
        for child in element:
            find_labels(child)

    # find labels starting from root
    find_labels(root)

    # sort and return labels
    return sorted(labels)
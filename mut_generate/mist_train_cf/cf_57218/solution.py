"""
QUESTION:
Implement a function `parse_XML(xml_file, desired_tags, ignore_tags)` that takes the name of an XML file, a list of desired tags, and a list of tags to ignore as input, and returns a dictionary where the keys are the desired tags and the values are lists of text content found within those tags in the XML file, excluding any text content within the ignored tags.
"""

import xml.etree.ElementTree as ET

def parse_XML(xml_file, desired_tags, ignore_tags):
    """
    This function takes the name of an XML file, a list of desired tags, 
    and a list of tags to ignore as input, and returns a dictionary where 
    the keys are the desired tags and the values are lists of text content 
    found within those tags in the XML file, excluding any text content 
    within the ignored tags.
    
    Parameters:
    xml_file (str): The name of the XML file.
    desired_tags (list): A list of desired tags.
    ignore_tags (list): A list of tags to ignore.
    
    Returns:
    dict: A dictionary with desired tags as keys and lists of text content as values.
    """
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    result = {}
    
    for tag in desired_tags:
        result[tag] = []

    def traverse(node):
        if node.tag in desired_tags and node.tag not in ignore_tags:
            result[node.tag].append(node.text)
            
        for child in node:
            traverse(child)

    traverse(root)
    return result
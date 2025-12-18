"""
QUESTION:
Create a function called `parse_xml` that takes an XML file as input and returns a dictionary where each key is a unique node tag and the value is a list of tuples containing the path of the node, its attributes, and its depth from the root node. The function should be able to parse multiple XML files and handle malformed or non-existent files. The output should be a comprehensive map of the relationship among all parsed XML files.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    dictionary = {}
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except ET.ParseError:
        print(f"XML file {xml_file} is malformed.")
        return dictionary
    except FileNotFoundError:
        print(f"XML file {xml_file} does not exist.")
        return dictionary

    def traverse_xml(root, path='', level=0):
        tag = root.tag.split('}')[-1]  # Get the tag without namespace
        if tag not in dictionary:
            dictionary[tag] = []
        attributes = root.attrib
        dictionary[tag].append((path, attributes, level))

        # Parse child nodes
        for child in root:
            child_path = path + '/' + tag
            traverse_xml(child, child_path, level+1)

    traverse_xml(root)
    return dictionary
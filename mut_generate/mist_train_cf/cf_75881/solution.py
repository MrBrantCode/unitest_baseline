"""
QUESTION:
Create a function to parse an XML file and generate an enumerated catalogue of its nodes, categorized by their occurrence count in descending order.

The function should take an XML file path as input and return a list of node names. The XML file is parsed, and each node's occurrence count is determined. The nodes are then categorized by their occurrence counts and sorted in descending order. Finally, an enumerated catalogue of node names is generated based on this categorization.

The input XML file path should be a string, and the output should be a list of strings representing the node names in the catalogue.
"""

import xml.etree.ElementTree as ET
from collections import defaultdict

def entrance(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    nodes_dict = defaultdict(int)
    for elem in root.iter():
        nodes_dict[elem.tag] += 1
    
    categorized_dict = defaultdict(list)
    for key, value in sorted(nodes_dict.items()):
        categorized_dict[value].append(key)
        
    catalogue = []
    for key in sorted(categorized_dict.keys(), reverse=True):
        catalogue.extend(categorized_dict[key])
    return catalogue
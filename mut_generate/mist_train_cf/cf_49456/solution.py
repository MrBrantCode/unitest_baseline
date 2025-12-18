"""
QUESTION:
Write a function `parse_xml` that takes an XML file as input and returns two lists. The first list contains the text content of all 'child' elements nested within 'parent' elements. The second list contains the text content of all 'grandchild' elements nested within the 'child' elements. The function should be able to find elements at any level beneath the root node. 

Note: The input XML file does not use namespaces.
"""

import xml.etree.ElementTree as ET

def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    children = root.findall('.//child')
    grandchildren = root.findall('.//grandchild')
    child_list = [child.text for child in children]
    grandchild_list = [grandchild.text for grandchild in grandchildren]
    return child_list, grandchild_list
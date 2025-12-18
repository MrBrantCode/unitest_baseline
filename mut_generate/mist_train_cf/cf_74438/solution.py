"""
QUESTION:
Create a function named `search` that takes in three parameters: the XML tree, an attribute name, and a value. The function should extract and return the details of a 'student' element from the XML tree based on the provided attribute and value. The search should also include nested tags within the 'student' tag.
"""

import xml.etree.ElementTree as ET

def search(tree, attribute, value):
    for student in tree.findall(".//student"):
        if student.attrib.get(attribute) == value:
            return student.attrib
        for child in student:
            if child.attrib.get(attribute) == value:
                return {**student.attrib, **child.attrib}            
    return None
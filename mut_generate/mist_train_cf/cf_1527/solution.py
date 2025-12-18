"""
QUESTION:
Write a function called `findElementsWithID` that recursively identifies all elements with the given ID attribute in a given XML document without using any built-in XML parsing libraries or functions. The function should take two parameters: `node` (the current XML node being processed) and `targetID` (the ID attribute being searched for), and return a list of elements with the given ID attribute.
"""

def findElementsWithID(node, targetID):
    result = []

    # Check if the current node has an ID attribute and if it matches the targetID
    if 'ID' in node.attributes and node.attributes['ID'] == targetID:
        result.append(node)

    # Recursively search nested elements
    for child in node.children:
        result += findElementsWithID(child, targetID)

    return result
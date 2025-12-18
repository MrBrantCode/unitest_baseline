"""
QUESTION:
Write a recursive function `findElementsWithID` that takes an XML document and a target ID attribute as input, and returns a list of all elements in the XML document with the given ID attribute. The function should have a time complexity of O(n), where n is the number of elements in the XML document.
"""

def findElementsWithID(xml_doc, target_id):
    result = []

    def traverse_elements(element):
        if "id" in element.attrib and element.attrib["id"] == target_id:
            result.append(element)

        for child in element:
            traverse_elements(child)

    traverse_elements(xml_doc.getroot())
    return result
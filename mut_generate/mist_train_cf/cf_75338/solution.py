"""
QUESTION:
Develop a function named `parse_book` that takes a string representing XML data as input. The function should identify and describe the elements within the 'book' label and any nested labels inside the 'book' label. It should also compute and display the total count of each unique attribute found within the 'book' labels. The function must handle cases where the root element is not 'book' and error handling for tags that do not adhere to the XML standard. The function should be case-sensitive and does not need to handle namespaces.
"""

from xml.etree.ElementTree import fromstring, ParseError
from collections import defaultdict

def parse_book(xml_str):
    try:
        root = fromstring(xml_str)
        if root.tag != 'book':
            print('The root element is not a book.')
            return

        book_attributes = dict(root.attrib)   # attributes of the book element
        nested_elements = defaultdict(dict)   # nested elements and their attributes
        attrib_counts = defaultdict(int)   # counts of unique attributes
        
        # Count book's attributes
        for attr in book_attributes:
            attrib_counts[attr] += 1
        
        # identify nested elements and count attributes
        for elem in root:
            nested_elements[elem.tag] = dict(elem.attrib)
            for attr in elem.attrib:
                attrib_counts[attr] += 1

        # display attributes and their counts
        print("Element: book \nAttributes:", book_attributes)
        for elem, attributes in nested_elements.items():
            print("Element:", elem, "\nAttributes:", attributes)
        print("Counts of unique attributes:", dict(attrib_counts))
        
    except ParseError:
        print('Invalid XML. Please ensure the tags adhere to XML standard.')
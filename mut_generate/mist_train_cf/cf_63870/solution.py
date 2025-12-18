"""
QUESTION:
Create an XML data structure to store classic literature pieces with their respective authors, publication dates, and main characters. The XML structure should have a root element named "classics" and child elements for each literature piece, including "title", "author", "publication_date", and a list of "character" elements under a "main_characters" element. Additionally, implement two search functions: `search_author(author_name)` and `search_literature(lit_name)`, which parse the XML file and return the XML element of the literature piece that matches the given author name or literature title, respectively. The search functions should return `None` if no match is found.
"""

import xml.etree.ElementTree as ET

def entrance(author_name=None, lit_name=None):
    """
    Searches for literature by author or title.

    Args:
    author_name (str): Name of the author to search for.
    lit_name (str): Title of the literature to search for.

    Returns:
    xml.etree.ElementTree.Element: XML element of the matching literature piece, or None if not found.
    """
    # parse the XML tree
    tree = ET.parse('classics.xml')
    root = tree.getroot()

    if author_name:
        # loop through each literature to search for the author
        for lit in root.findall('literature'):
            author = lit.find('author').text
            if author == author_name:
                # return literature details
                return lit
    elif lit_name:
        # loop through each literature to search for the title
        for lit in root.findall('literature'):
            title = lit.find('title').text
            if title == lit_name:
                # return literature details
                return lit
    return None
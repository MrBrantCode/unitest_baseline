"""
QUESTION:
Write a function named `dict_to_xml` that takes a list of dictionaries as input where each dictionary represents a book with keys 'title', 'author', and 'year'. The function should return a formatted XML string representation of the input data with each book as a separate "Book" element under the root "Books" element, and include tags for each data type (title, author, and year).
"""

import xml.etree.ElementTree as ET

def dict_to_xml(data):
    """
    Converts a list of dictionaries into an XML string.

    Args:
        data (list): A list of dictionaries, each representing a book with keys 'title', 'author', and 'year'.

    Returns:
        str: An XML string representation of the input data.
    """

    # creating the root element
    root = ET.Element("Books")

    # iterating over each element in the data list
    for book in data:
        # creating a "Book" element
        book_elem = ET.SubElement(root, "Book")
        
        # creating a "Title", "Author", and "Year" element for each book
        # and assigning their text to the respective values in the current dictionary
        ET.SubElement(book_elem, "Title").text = book['title']
        ET.SubElement(book_elem, "Author").text = book['author']
        ET.SubElement(book_elem, "Year").text = str(book['year'])  # convert int to str for XML

    # converting the ElementTree to a string with pretty printing
    return ET.tostring(root, encoding="UTF-8", method="xml").decode()
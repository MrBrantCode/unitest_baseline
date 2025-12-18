"""
QUESTION:
Write a function `find_book` that takes an XML string and a book ID as input, and returns the title and author of the book with the given ID. If the book ID is not found, return an error message. The XML string represents a nested library structure with sections and books, where each book has an ID, title, and author.
"""

import xml.etree.ElementTree as ET

def find_book(xml_string, book_id):
    """
    This function takes an XML string and a book ID as input, 
    and returns the title and author of the book with the given ID.

    Args:
        xml_string (str): A string representing the XML structure of a library.
        book_id (str): The ID of the book to be searched.

    Returns:
        tuple: A tuple containing the title and author of the book if found. 
               Otherwise, returns an error message.
    """
    root = ET.fromstring(xml_string)
    for book in root.iter('book'):
        if book.attrib['id'] == book_id:
            title = book.find('title').text
            author = book.find('author').text
            return title, author
    return "Book not found."
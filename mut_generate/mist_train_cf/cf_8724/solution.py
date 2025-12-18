"""
QUESTION:
Extract the title and author of a specific book with a given ID from an XML structure.

Implement a function `extract_book_details(xml_str, book_id)` that takes two parameters: an XML string `xml_str` representing a library of books and a `book_id`. The function should iterate over the book elements in the XML structure, find the book with the matching `book_id`, and return its title and author if the book is available for borrowing. If the book is not found or not available, the function should return an error message. 

The function should have a time complexity of O(n), where n is the total number of books in the XML structure, and a space complexity of O(1).
"""

import xml.etree.ElementTree as ET

def extract_book_details(xml_str, book_id):
    # Parse the XML string
    root = ET.fromstring(xml_str)
    
    # Iterate over the book elements
    for book in root.iter('book'):
        if book.attrib['id'] == book_id:
            # Check if the book is available for borrowing
            if book.attrib['available'] == 'yes':
                # Extract the title and author
                title = book.find('title').text
                author = book.find('author').text
                return title, author
            else:
                return 'Book is not available for borrowing.'
    
    # Book with the given ID not found
    return 'Book ID not found.'
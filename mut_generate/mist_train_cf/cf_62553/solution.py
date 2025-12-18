"""
QUESTION:
Create a function called `parse_bookstore` that takes a string of XML data representing a bookstore's inventory as input. The XML data should be parsed to extract the title, author, and price of each book, and return this information in a readable format. The function should be able to handle an XML structure with a nested 'bookstore' element containing multiple 'book' elements, each with 'title', 'author', and 'price' elements.
"""

import xml.etree.ElementTree as ET

def parse_bookstore(xml_data):
    """
    This function takes a string of XML data representing a bookstore's inventory as input.
    It parses the XML to extract the title, author, and price of each book, 
    and returns this information in a readable format.

    Args:
        xml_data (str): A string of XML data representing a bookstore's inventory.

    Returns:
        list: A list of dictionaries where each dictionary contains the title, author, and price of a book.
    """
    root = ET.fromstring(xml_data)
    books = []

    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        price = book.find('price').text

        books.append({
            'title': title,
            'author': author,
            'price': price
        })

    return books
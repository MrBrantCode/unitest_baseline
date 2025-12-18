"""
QUESTION:
Create a function named `parse_xml` that takes a string representing an XML document as input. The XML document has a root element named `books` that contains multiple `book` elements, each with `title`, `price`, and `ratings` elements. The `ratings` element contains multiple `rating` elements. The function should return the total price of all the books and a list of dictionaries, where each dictionary contains the title, price, and average rating of a book. The list should be sorted in descending order of the average rating.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    
    books = []
    total_price = 0
    
    for book_elem in root.findall('book'):
        title = book_elem.find('title').text
        price = float(book_elem.find('price').text)
        ratings = [int(rating_elem.text) for rating_elem in book_elem.find('ratings').findall('rating')]
        average_rating = sum(ratings) / len(ratings)
        
        book = {
            'title': title,
            'price': price,
            'average_rating': average_rating
        }
        
        books.append(book)
        total_price += price
    
    books.sort(key=lambda x: x['average_rating'], reverse=True)
    
    return total_price, books
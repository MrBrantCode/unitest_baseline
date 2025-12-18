"""
QUESTION:
Write a function `parse_xml` that takes a string representing a well-formed XML document as input, parses the document, and calculates the total price of all the books in the bookstore. The function should also calculate the average rating for each book and return the total price along with a list of dictionaries, where each dictionary contains the title, price, and average rating of a book. The list should be sorted in descending order of the average rating.
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
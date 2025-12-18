"""
QUESTION:
Function: `parse_xml(xml_string)`

Given an XML string representing a list of books with their titles, prices, and user ratings, calculate the total price of all books and the average rating for each book. The XML structure consists of a root element `books` containing multiple `book` elements, each with `title`, `price`, and `ratings` elements.

The function should return the total price of all books and a list of dictionaries, where each dictionary contains the title, price, and average rating of a book. The list should be sorted in descending order of the average rating.

Constraints: The maximum number of books is 1000, the maximum number of ratings per book is 100, the maximum title length is 100 characters, the maximum XML document length is 10^6 characters, the maximum rating value is 10, and the maximum price value is 10^6.
"""

import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    books = root.findall('book')
    total_price = 0
    book_list = []
    
    for book in books:
        title = book.find('title').text
        price = float(book.find('price').text)
        ratings = book.find('ratings').findall('rating')
        total_rating = 0
        
        for rating in ratings:
            total_rating += int(rating.text)
        
        average_rating = total_rating / len(ratings)
        total_price += price
        
        book_dict = {
            'title': title,
            'price': price,
            'average_rating': average_rating
        }
        book_list.append(book_dict)
    
    sorted_book_list = sorted(book_list, key=lambda x: x['average_rating'], reverse=True)
    
    return total_price, sorted_book_list
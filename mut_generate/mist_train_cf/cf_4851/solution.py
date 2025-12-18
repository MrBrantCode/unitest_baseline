"""
QUESTION:
Function name: `parse_xml`

Given an XML string representing a bookstore with a list of books, each containing a title, price, and user ratings, write a function to calculate the total price of all the books and the average rating for each book. The function should return the total price and a list of dictionaries, where each dictionary contains the title, price, and average rating of a book. The list should be sorted in descending order of the average rating.

Constraints:

- Maximum number of books in the XML document: 1000
- Maximum number of ratings for each book: 100
- Maximum number of characters in the title of each book: 100
- Maximum number of characters in the XML document: 10^6
- Maximum value of each rating: 10
- Maximum value of the price: 10^6
"""

import xml.etree.ElementTree as ET

def entrance(xml_string):
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
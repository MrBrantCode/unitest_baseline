"""
QUESTION:
Create a function `filter_books_by_year` that takes a JSON file containing a list of books as input, where each book has the fields "title", "author", and "year". The function should return a list of books that were published after the year 1980.

Restrictions: The input JSON file has the following structure: a single key "books" that maps to a list of book objects. Each book object has a "year" field, which is a string representing the year of publication. The function should correctly handle the conversion of the "year" field to an integer for comparison with the target year 1980.
"""

import json

def filter_books_by_year(data):
    """
    This function filters a list of books by year and returns books published after 1980.

    Args:
        data (dict): A dictionary containing a list of books with "title", "author", and "year" fields.

    Returns:
        list: A list of books published after 1980.
    """
    books = data['books']
    return [book for book in books if int(book['year']) > 1980]
"""
QUESTION:
Design a function named `group_books` that uses the `groupby` function from the `itertools` module to sort and group a list of dictionaries by a given key. The function should accept a list of dictionaries where each dictionary represents a book with the keys "author", "title", and "year_published". The function should first sort the list by the "author" and then by the "year_published", and then group the books by the "author" and "year_published". The function should return a sorted and grouped list of books. Note that the `groupby` function only groups consecutive items together, so the list must be sorted first.
"""

from operator import itemgetter
from itertools import groupby

def group_books(books_list):
    """
    Sorts and groups a list of dictionaries by the "author" and "year_published" keys.
    
    Args:
        books_list (list): A list of dictionaries where each dictionary represents a book.
    
    Returns:
        A sorted and grouped list of books.
    """
    # Define the key to sorting and grouping
    sortKeyFunc = itemgetter("author", "year_published")
    
    # Sort the list by the "author" and "year_published"
    books_list.sort(key=sortKeyFunc)
    
    # Group the books by the "author" and "year_published"
    grouped_books = groupby(books_list, sortKeyFunc)
    
    return grouped_books
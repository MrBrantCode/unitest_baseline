"""
QUESTION:
Create a function `sort_books_by_rating` that takes a list of dictionaries, each representing a book with keys "title", "author", "publication date", and "rating". The function should sort the books based on their rating in descending order and return a JSON string representing the sorted list of books.
"""

import json

def sort_books_by_rating(books):
    """
    Sorts a list of book dictionaries by rating in descending order and returns a JSON string.

    Args:
        books (list): A list of dictionaries, each representing a book with keys "title", "author", "publication date", and "rating".

    Returns:
        str: A JSON string representing the sorted list of books.
    """
    sorted_books = sorted(books, key=lambda x: x["rating"], reverse=True)
    return json.dumps(sorted_books, indent=4)
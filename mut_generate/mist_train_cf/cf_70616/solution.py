"""
QUESTION:
Create a function `get_books_after_year` that takes a list of book dictionaries and a specific year as input, and returns a list of dictionaries representing books published after the given year. Each book dictionary should have a 'title' key and a 'year' key.
"""

def get_books_after_year(books, year):
    """
    Returns a list of dictionaries representing books published after the given year.

    Args:
        books (list): A list of dictionaries where each dictionary represents a book.
        year (int): The year to filter books by.

    Returns:
        list: A list of dictionaries representing books published after the given year.
    """
    return [book for book in books if book['year'] > year]
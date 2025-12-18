"""
QUESTION:
Create a Python function named `classify_book` that takes a dictionary representing a book with keys for Title, Author, Publisher, Publication Year, and Genre as input and returns the genre of the book. The function should work with a pandas dataframe where each row represents a book.
"""

def classify_book(book_dict):
    """Returns the genre of a book given a dictionary with book information."""
    return book_dict['Genre']
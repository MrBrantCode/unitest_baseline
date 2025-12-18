"""
QUESTION:
Create a function called `classify_book` that takes a dictionary with keys for Title, Author, Publisher, Publication Year, and Genre, and returns the genre of the book.
"""

def classify_book(book_dict):
    """
    Returns the genre of a book given a dictionary with book details.

    Args:
    book_dict (dict): A dictionary containing book details with keys 'Title', 'Author', 'Publisher', 'Publication Year', and 'Genre'.

    Returns:
    str: The genre of the book.
    """
    return book_dict['Genre']
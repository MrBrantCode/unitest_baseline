"""
QUESTION:
Create a function `classify_book` that takes a dictionary containing keys for 'Title', 'Author', 'Publisher', 'Publication Year', and 'Genre' as input and returns the 'Genre' of the book.
"""

def classify_book(book_dict):
    """
    This function takes a dictionary containing book information and returns the 'Genre' of the book.

    Args:
        book_dict (dict): A dictionary containing keys for 'Title', 'Author', 'Publisher', 'Publication Year', and 'Genre'.

    Returns:
        str: The 'Genre' of the book.
    """
    genre = book_dict['Genre']
    return genre
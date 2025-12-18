"""
QUESTION:
Create a function named `classify_book` that takes a dictionary with keys 'Title', 'Author', 'Publisher', 'Publication Year', and 'Genre' as input and returns the 'Genre' value from the dictionary.
"""

def classify_book(book_dict):
    genre = book_dict['Genre']
    return genre
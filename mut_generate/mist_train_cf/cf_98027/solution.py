"""
QUESTION:
Create a function `get_recommended_books` that takes two dictionaries as input: `books` and `publication_dates`. The `books` dictionary has genres as keys and lists of book titles as values, and the `publication_dates` dictionary has book titles as keys and their publication dates as values. The function should return a dictionary where the keys are genres and the values are dictionaries with two keys: "recommended_books" and "all_books". For the "Fantasy" genre, "recommended_books" should contain the most recently published book, and for the "Horror" genre, "recommended_books" should contain the oldest published book. The "all_books" key should contain all books in the genre, sorted by publication date.
"""

def get_recommended_books(books, publication_dates):
    """
    Returns a dictionary where the keys are genres and the values are dictionaries 
    with two keys: "recommended_books" and "all_books". For the "Fantasy" genre, 
    "recommended_books" contains the most recently published book, and for the "Horror" 
    genre, "recommended_books" contains the oldest published book. The "all_books" key 
    contains all books in the genre, sorted by publication date.

    Args:
        books (dict): A dictionary with genres as keys and lists of book titles as values.
        publication_dates (dict): A dictionary with book titles as keys and their publication dates as values.

    Returns:
        dict: A dictionary with genres as keys and dictionaries with "recommended_books" and "all_books" as values.
    """
    recommended_books = {}
    for genre, books_list in books.items():
        sorted_books = sorted(books_list, key=lambda x: publication_dates[x])
        if genre == "Fantasy":
            recommended_books[genre] = {
                "recommended_books": [sorted_books[-1]],  # most recently published book
                "all_books": sorted_books
            }
        elif genre == "Horror":
            recommended_books[genre] = {
                "recommended_books": [sorted_books[0]],  # oldest published book
                "all_books": sorted_books
            }
        else:
            recommended_books[genre] = {
                "recommended_books": [],
                "all_books": sorted_books
            }
    return recommended_books
"""
QUESTION:
Create a function `BookSearch` that takes a search term as input and returns a list of book dictionaries with titles containing the search term. The function should be case-insensitive and return the results in JSON format. The list of books is predefined as a list of dictionaries with 'title' and 'author' keys. 

The function should be part of a RESTful API and accessible via a URL path '/search/<string:search_term>'.
"""

def BookSearch(books, search_term):
    """
    This function searches for books in the given list that contain the search term in their titles.
    
    Args:
    books (list): A list of dictionaries where each dictionary represents a book with 'title' and 'author' keys.
    search_term (str): The term to be searched in the book titles.
    
    Returns:
    list: A list of dictionaries representing books whose titles contain the search term.
    """
    results = [book for book in books if search_term.lower() in book['title'].lower()]
    return results
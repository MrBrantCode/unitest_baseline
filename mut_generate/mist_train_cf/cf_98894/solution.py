"""
QUESTION:
Create a function named `get_high_rated_books` that takes in a list of books and a publisher name. The function should return a list of tuples, where each tuple contains the title and author of a book published by the specified publisher and having a rating of 4.0 or above. The returned list should be sorted alphabetically by the author's last name.
"""

def get_high_rated_books(books, publisher):
    """
    Returns a list of tuples containing the title and author of books 
    published by the specified publisher with a rating of 4.0 or above, 
    sorted alphabetically by the author's last name.

    Args:
    books (list): A list of dictionaries representing books.
    publisher (str): The name of the publisher.

    Returns:
    list: A list of tuples containing the title and author of high rated books.
    """

    high_rated_books = [
        (book['title'], book['author']) 
        for book in books 
        if book['publisher'] == publisher and book['rating'] >= 4.0
    ]

    # Sort the high rated books list by author's last name
    high_rated_books.sort(key=lambda x: x[1].split()[-1])

    return high_rated_books
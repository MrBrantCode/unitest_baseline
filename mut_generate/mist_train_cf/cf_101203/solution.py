"""
QUESTION:
Create a function named `get_high_rated_books` that takes a list of books and a specific publisher as input. The function should filter the books published by the given publisher with a rating of 4.0 or above. It should then return a new list containing the titles and authors of the filtered books, sorted alphabetically by the author's last name. The input list of books is a list of dictionaries, where each dictionary contains the keys 'title', 'author', 'publisher', and 'rating'.
"""

def get_high_rated_books(books, publisher):
    """
    Filter books published by the given publisher with a rating of 4.0 or above.
    Return a new list containing the titles and authors of the filtered books, 
    sorted alphabetically by the author's last name.

    Args:
    books (list): A list of dictionaries, where each dictionary contains the keys 
                  'title', 'author', 'publisher', and 'rating'.
    publisher (str): The specific publisher to search for.

    Returns:
    list: A list of tuples containing the titles and authors of the filtered books.
    """

    # Filter the books published by the given publisher with a rating of 4.0 or above
    high_rated_books = [book for book in books 
                        if book['publisher'] == publisher and book['rating'] >= 4.0]

    # Sort the high rated books list by author's last name
    high_rated_books.sort(key=lambda x: x['author'].split()[-1])

    # Return a list of tuples containing the titles and authors of the filtered books
    return [(book['title'], book['author']) for book in high_rated_books]
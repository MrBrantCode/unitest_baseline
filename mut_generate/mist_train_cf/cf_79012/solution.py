"""
QUESTION:
Create a function called `classify_books_by_nationality` that takes two parameters: a list of books where each book is a dictionary containing 'title' and 'author', and a list of authors where each author is a dictionary containing 'name' and 'nationality'. The function should return a dictionary where the keys are nationalities and the values are lists of books written by authors of that nationality. If an author's nationality is not found, the book should be categorized under 'Unknown'.
"""

def classify_books_by_nationality(books, authors):
    """
    This function takes a list of books and authors, and returns a dictionary where the keys are nationalities and the values are lists of books written by authors of that nationality.

    Args:
        books (list): A list of dictionaries where each dictionary contains 'title' and 'author'.
        authors (list): A list of dictionaries where each dictionary contains 'name' and 'nationality'.

    Returns:
        dict: A dictionary where the keys are nationalities and the values are lists of books.
    """

    # Create a dictionary to store the nationality of each author
    author_nationality = {author['name']: author['nationality'] for author in authors}

    # Initialize an empty dictionary to store the result
    result = {}

    # Iterate over each book
    for book in books:
        # Get the author's name from the book
        author_name = book['author']

        # Get the author's nationality from the author_nationality dictionary
        # If the author's nationality is not found, categorize the book as 'Unknown'
        nationality = author_nationality.get(author_name, 'Unknown')

        # If the nationality is not already a key in the result dictionary, add it
        if nationality not in result:
            result[nationality] = []

        # Add the book to the list of books for the author's nationality
        result[nationality].append(book)

    return result
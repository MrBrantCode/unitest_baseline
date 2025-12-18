"""
QUESTION:
Create a function `search_books` that takes in a dictionary `books` containing a nested structure of books, a string `genre`, and an integer `min_rating`. The dictionary contains a list of books categorized into different genres, with each book having a unique identifier, title, author, publication year, characters, tags, and readers with ratings. Implement the function to return a list of books that match the given genre and have a minimum rating, sorted by their publication year in ascending order.
"""

def search_books(books, genre, min_rating):
    """
    Searches for books in the given genre with a minimum rating and returns them sorted by publication year.

    Args:
        books (dict): A dictionary of books with nested structure.
        genre (str): The genre to search for.
        min_rating (int): The minimum rating of the books to include.

    Returns:
        list: A list of books that match the given genre and have a minimum rating, sorted by publication year.
    """

    # Calculate the minimum rating as the average of the readers' ratings
    def calculate_min_rating(book):
        return sum(reader["rating"] for reader in book["readers"]) / len(book["readers"])

    # Filter books by genre and minimum rating
    matching_books = [book for book in books.get(genre, []) if calculate_min_rating(book) >= min_rating]
    
    # Sort the matching books by publication year
    matching_books.sort(key=lambda x: x["publication_year"])
    
    return matching_books
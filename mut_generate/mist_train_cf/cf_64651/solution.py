"""
QUESTION:
Implement a function to rate books with the following restrictions: 
- The function should be named rate_book 
- The function should be able to handle multiple book ratings 
- The function should be able to return the average rating for a specific book 
- No additional information is provided
"""

def rate_book(ratings):
    """
    Calculate the average rating for a specific book.

    Args:
    ratings (dict): A dictionary where keys are book names and values are lists of ratings.

    Returns:
    dict: A dictionary where keys are book names and values are their average ratings.
    """
    average_ratings = {}
    for book, book_ratings in ratings.items():
        average_ratings[book] = sum(book_ratings) / len(book_ratings)
    return average_ratings
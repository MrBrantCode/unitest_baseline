"""
QUESTION:
Given a total time frame and the time required to complete each book, write a function named `calculate_books` that takes two parameters: `total_time` and `time_per_book`, and returns the total number of books that can be finished within the given time frame. The function should divide the total time by the time needed for each book and return the result.
"""

def calculate_books(total_time, time_per_book):
    """
    Calculate the total number of books that can be finished within a given time frame.
    
    Parameters:
    total_time (float): The total time frame available.
    time_per_book (float): The time required to complete each book.
    
    Returns:
    float: The total number of books that can be finished.
    """
    return total_time / time_per_book
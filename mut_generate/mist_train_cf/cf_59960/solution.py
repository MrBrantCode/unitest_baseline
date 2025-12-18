"""
QUESTION:
Design a function named `get_available_seats` to display the available seats for a specific movie show in a theater. The function should take two parameters: `movie_show_id` and `theater_layout`. The `movie_show_id` is a unique identifier for the movie show, and the `theater_layout` is a 2D list representing the seating arrangement of the theater, where 0 represents an empty seat and 1 represents a reserved seat. The function should return a list of available seats in the format (row, column).
"""

def get_available_seats(movie_show_id, theater_layout):
    """
    Returns a list of available seats in the format (row, column) for a specific movie show in a theater.

    Args:
        movie_show_id (int): A unique identifier for the movie show.
        theater_layout (list): A 2D list representing the seating arrangement of the theater, 
                              where 0 represents an empty seat and 1 represents a reserved seat.

    Returns:
        list: A list of available seats in the format (row, column).
    """
    available_seats = [(row, col) for row in range(len(theater_layout)) 
                       for col in range(len(theater_layout[row])) 
                       if theater_layout[row][col] == 0]
    return available_seats
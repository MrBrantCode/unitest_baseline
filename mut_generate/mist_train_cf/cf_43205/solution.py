"""
QUESTION:
Create a function `serialize_movie` that takes a movie object with attributes `title`, `year`, and `genre` as input and returns a serialized output in the following format:
- status (boolean): Indicates the status of the serialization
- data (nested): Contains the serialized movie data with fields `title`, `year`, and `genre`
- message (string): Provides additional information about the serialization

The serialized output should have a nested structure, where the `data` field contains the serialized movie data. The function should return the serialized output in a dictionary format.
"""

def serialize_movie(movie_obj):
    """
    Serialize a movie object into a dictionary format.

    Args:
        movie_obj (object): A movie object with attributes title, year, and genre.

    Returns:
        dict: A dictionary containing the serialized movie data.
    """
    serialized_movie = {
        'status': True,  # Assuming successful serialization
        'data': {
            'title': movie_obj.title,
            'year': movie_obj.year,
            'genre': movie_obj.genre
        },
        'message': 'Movie serialized successfully'
    }
    return serialized_movie
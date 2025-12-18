"""
QUESTION:
Write a function named `movie_rating_restrictions` that takes an integer age as input and returns a string indicating the movie rating restrictions based on the following rules: 
- If the age is less than 13, the viewer may only see G and PG movies.
- If the age is 13 or older but less than 17, the viewer can see any movies except for R-rated movies.
- If the age is 17 or older, the viewer can watch any rated movie.
"""

def movie_rating_restrictions(age: int) -> str:
    """
    Determine the movie rating restrictions based on the viewer's age.

    Args:
    age (int): The age of the viewer.

    Returns:
    str: A string indicating the movie rating restrictions.
    """
    if age < 13:
        return "You may only see G and PG movies"
    elif 13 <= age < 17:
        return "You can see any movies except for R movies"
    else:
        return "You can watch any rated movie"
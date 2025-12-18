"""
QUESTION:
Create a function called `best_picture_info` that takes the title of a "Best Picture" winning movie and its corresponding director as input. The function should return a dictionary with the movie's accolades, theatrical run duration, and the director's previous works. The dictionary should also contain a feature to compare the movie's impact on popular culture and its critical reception. Assume the required data is available and can be fetched.
"""

def best_picture_info(title, director):
    """
    Returns a dictionary containing information about the movie's accolades, 
    theatrical run duration, and the director's previous works. It also 
    compares the movie's impact on popular culture and its critical reception.

    Parameters:
    title (str): The title of the "Best Picture" winning movie.
    director (str): The director of the movie.

    Returns:
    dict: A dictionary containing the movie's information.
    """

    # Assuming the required data is available and can be fetched
    movie_data = {
        "accolades": {"awards": ["Oscar", "Golden Globe"], "nominations": 10},
        "theatrical_run": {"start_date": "2020-01-01", "end_date": "2020-06-30"},
        "director": {"previous_works": ["Movie1", "Movie2"]},
        "impact": {"popular_culture": "High", "critical_reception": "Positive"}
    }

    return movie_data
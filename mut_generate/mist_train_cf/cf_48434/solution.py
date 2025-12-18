"""
QUESTION:
Create a data dictionary to store information about a multi-lingual micro-budget independent film. The dictionary should be able to handle diverse character inputs and include fields for film details, translation, and subtitling. The data structure should be capable of storing information for multiple films, each with multiple translations and subtitles.
"""

def create_film_data_dict(film_id):
    """
    Create a data dictionary to store information about a multi-lingual micro-budget independent film.

    Args:
        film_id (str): A unique identifier for the film.

    Returns:
        dict: A dictionary containing the film's information, translations, and subtitles.
    """
    return {
        film_id: {
            "film_name": "",
            "film_language": "",
            "film_budget": 0.0,
            "film_director": "",
            "film_cast": [],
            "film_release_date": "",
            "subtitles": [
                {
                    "subtitle_language": "",
                    "subtitle_file": ""
                },
            ],
            "translations": [
                {
                    "translated_language": "",
                    "translated_title": "",
                    "translated_synopsis": "",
                },
            ]
        }
    }
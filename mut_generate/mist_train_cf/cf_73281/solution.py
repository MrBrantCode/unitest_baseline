"""
QUESTION:
Design a function called `create_oscar_experience` that takes the name of a film, its director, the number of awards it has won, the duration it stayed in theaters, the box office earnings of the film and the director's past films, and the number of awards won by each of the director's past films. The function should return a design outline for an interactive augmented reality experience that showcases the film, amplifies the visual elements to reflect the number of awards the film has won, displays the duration each film has stayed in theaters, and contrasts the director's current film with their past films in terms of box office earnings and awards.
"""

def create_oscar_experience(film_name, director, awards_won, duration_in_theaters, box_office_earnings, past_films, past_awards):
    """
    This function generates a design outline for an interactive augmented reality experience 
    showcasing a film, its director, awards won, duration in theaters, box office earnings, 
    and the director's past films.

    Args:
    film_name (str): The name of the film.
    director (str): The director of the film.
    awards_won (int): The number of awards the film has won.
    duration_in_theaters (str): The duration the film stayed in theaters.
    box_office_earnings (float): The box office earnings of the film.
    past_films (list): A list of the director's past films.
    past_awards (list): A list of the number of awards won by each of the director's past films.

    Returns:
    dict: A dictionary representing the design outline for the AR experience.
    """
    design_outline = {
        "entry_point": {
            "description": f"User starts the AR experience with a large golden Oscar statuette. The statuette can be placed anywhere in the room and it functions as the menu or entry point of the experience.",
            "film_name": film_name,
            "director": director
        },
        "best_picture_highlight": {
            "description": f"The name and poster image of the 'Best Picture' winner film unfolds, creating an immersive 3D scene environment echoing the film's setting and theme.",
            "film_name": film_name,
            "director": director
        },
        "award_count_visualization": {
            "description": f"The number of other awards the film has won are displayed as smaller statuettes orbiting around the main Oscar statuette.",
            "awards_won": awards_won
        },
        "duration_display": {
            "description": f"The time the movie stayed in theaters would be represented by a timeline inside the 3D scene.",
            "duration_in_theaters": duration_in_theaters
        },
        "box_office_earnings_and_past_successes": {
            "description": f"A virtual screen would pop up with a line graph contrasting the box office earnings of all the director's films. A separate bar graph would show the number of awards each film has won.",
            "box_office_earnings": box_office_earnings,
            "past_films": past_films,
            "past_awards": past_awards
        },
        "directors_film_portfolio": {
            "description": f"The environment would change to reflect the chosen film's theme and setting, providing a unique and immersive way to explore each film.",
            "past_films": past_films
        },
        "user_interface": {
            "description": f"For user-friendly navigation, there would be a simple and intuitive interface."
        }
    }
    return design_outline
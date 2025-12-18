"""
QUESTION:
Determine the most suitable programming language for a web application development project, considering efficiency, scalability, and ease of use.
"""

def most_suitable_language(efficiency, scalability, ease_of_use):
    """
    Determine the most suitable programming language for a web application development project.

    Parameters:
    efficiency (float): A value between 0 and 1 representing the required efficiency.
    scalability (float): A value between 0 and 1 representing the required scalability.
    ease_of_use (float): A value between 0 and 1 representing the required ease of use.

    Returns:
    str: The most suitable programming language for the given requirements.
    """
    
    languages = {
        "Python": (0.8, 0.9, 0.8),
        "JavaScript": (0.7, 0.8, 0.9),
        "Ruby": (0.6, 0.7, 0.8),
        "Java": (0.9, 0.9, 0.5),
        "PHP": (0.5, 0.6, 0.7),
        "Go": (0.9, 0.8, 0.6)
    }

    best_language = None
    best_score = 0

    for language, (eff, scale, ease) in languages.items():
        score = (eff * efficiency + scale * scalability + ease * ease_of_use) / (efficiency + scalability + ease_of_use)
        if score > best_score:
            best_score = score
            best_language = language

    return best_language
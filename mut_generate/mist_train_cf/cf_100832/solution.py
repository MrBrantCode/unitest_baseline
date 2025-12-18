"""
QUESTION:
Write a function `get_supported_languages` that takes two inputs: a dictionary `languages` where the keys are programming language names and the values are lists of their specifications, and a list `features` containing the required features. The function should return a list of programming languages that support all the features in the `features` list, sorted by their name length.
"""

def get_supported_languages(languages, features):
    """
    Returns a list of programming languages that support all the features in the features list, sorted by their name length.

    Args:
    languages (dict): A dictionary where the keys are programming language names and the values are lists of their specifications.
    features (list): A list containing the required features.

    Returns:
    list: A list of programming languages that support all the features in the features list, sorted by their name length.
    """
    return sorted([language for language, specs in languages.items() if all(feature in specs for feature in features)], key=len)
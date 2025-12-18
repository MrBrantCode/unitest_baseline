"""
QUESTION:
Create a function named `get_supported_languages` that takes in two parameters: a dictionary `languages` where the keys are programming language names and the values are lists of features, and a list `features` containing the required features. The function should return a list of programming languages that support all the features in the `features` list, sorted by their names.
"""

def get_supported_languages(languages, features):
    """
    Returns a list of programming languages that support all the features in the features list, sorted by their names.

    Args:
        languages (dict): A dictionary where the keys are programming language names and the values are lists of features.
        features (list): A list containing the required features.

    Returns:
        list: A list of programming languages that support all the features in the features list, sorted by their names.
    """
    supported_languages = [language for language, specs in languages.items() if all(feature in specs for feature in features)]
    supported_languages.sort()
    return supported_languages
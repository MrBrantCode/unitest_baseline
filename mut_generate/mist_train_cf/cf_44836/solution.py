"""
QUESTION:
Write a function called `get_default_language` that returns the default language of an application based on the installation location and the supported languages. The function should take two parameters: `installation_location` (a string representing the location where the software is being installed) and `supported_languages` (a dictionary where the keys are the supported languages and the values are their corresponding locale codes). The function should return the default language in the format "language (locale code)". If the installation location is not supported, the function should return "English (en)" as the default language.
"""

def get_default_language(installation_location, supported_languages):
    """
    Returns the default language of an application based on the installation location and the supported languages.

    Args:
        installation_location (str): The location where the software is being installed.
        supported_languages (dict): A dictionary where the keys are the supported languages and the values are their corresponding locale codes.

    Returns:
        str: The default language in the format "language (locale code)".
    """

    # Check if the installation location is supported
    if installation_location in supported_languages:
        # Return the default language in the format "language (locale code)"
        return f"{installation_location} ({supported_languages[installation_location]})"
    else:
        # Return "English (en)" as the default language if the installation location is not supported
        return "English (en)"
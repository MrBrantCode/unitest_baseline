"""
QUESTION:
Create an Auto-Complete Provider function for a specific language that analyzes the syntax of a given language and provides word suggestions while typing in the source code. The function should be able to detect the language type from the file extension and provide the auto-complete suggestions accordingly.
"""

import os

def auto_complete_provider(file_path, typed_text):
    """
    This function provides word suggestions based on the language detected from the file extension.

    Args:
        file_path (str): The path to the file.
        typed_text (str): The text that the user has typed so far.

    Returns:
        list: A list of word suggestions.
    """

    # Detect the language type from the file extension
    _, file_extension = os.path.splitext(file_path)
    language = file_extension[1:].lower()

    # Dictionary to store language-specific keywords and functions
    language_keywords = {
        "js": ["javascript", "console", "log", "function"],
        "py": ["python", "print", "def", "class"],
        # Add more languages as needed
    }

    # Get the language-specific keywords
    suggestions = [keyword for keyword in language_keywords.get(language, []) if keyword.startswith(typed_text)]

    return suggestions
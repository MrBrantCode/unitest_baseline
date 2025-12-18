"""
QUESTION:
Write a function called `member_variable_prefix` that takes a string parameter `language` representing the programming language being used, and returns a commonly used prefix style for member variables in that language. The function should return one of the following prefixes: `_` (underscore), `m` (lowercase 'm'), or an empty string (no prefix).
"""

def member_variable_prefix(language):
    """
    Returns a commonly used prefix style for member variables in a given programming language.
    
    Args:
        language (str): The programming language being used.
    
    Returns:
        str: A prefix style for member variables in the given language.
    """
    prefix_styles = {
        "Python": "_",
        "C++": "_",
        "Objective-C": "_",
        "Java": "m",
    }
    
    return prefix_styles.get(language, "")
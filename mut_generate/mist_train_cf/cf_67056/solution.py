"""
QUESTION:
Create a function called `is_enclosed_by` that takes two string parameters, `str` and `substring`, and returns a boolean value indicating whether `str` is enclosed by `substring` with no overlapping instances.
"""

def is_enclosed_by(s, substring):
    """
    Checks if a given string is enclosed by a substring with no overlapping instances.

    Args:
    s (str): The main string to check.
    substring (str): The substring to check for.

    Returns:
    bool: True if the string is enclosed by the substring with no overlapping instances, False otherwise.
    """
    if not substring:
        return False  # Return False for an empty substring

    if len(substring) > len(s):
        return False  # Return False if substring is longer than the main string

    # Check if the string starts and ends with the substring
    if s.startswith(substring) and s.endswith(substring):
        # Remove the first and last occurrences of the substring
        temp_str = s[len(substring):-len(substring)]
        # Check for any remaining occurrences of the substring
        return substring not in temp_str
    return False
"""
QUESTION:
HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

The sorting should **NOT** be case sensitive
"""

def sort_textbooks(textbooks):
    """
    Sorts a list of textbook titles in a case-insensitive manner.

    Parameters:
    textbooks (list of str): A list of textbook titles to be sorted.

    Returns:
    list of str: A sorted list of textbook titles.
    """
    return sorted(textbooks, key=str.lower)
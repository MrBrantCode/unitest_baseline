"""
QUESTION:
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
"""

def remove_duplicate_words(s: str) -> str:
    """
    Removes all duplicate words from a string, leaving only the first occurrence of each word.

    Parameters:
    s (str): The input string containing words.

    Returns:
    str: A string with all duplicate words removed.
    """
    return ' '.join(dict.fromkeys(s.split()))
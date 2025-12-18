"""
QUESTION:
Create a function `sort_statements_by_vowels` that takes a list of strings as input and returns the sorted list in ascending order based on the number of vowels in each string. The function should ignore case and non-alphabetic characters.
"""

def sort_statements_by_vowels(statements):
    """
    Sorts a list of strings in ascending order based on the number of vowels in each string.
    
    Args:
        statements (list): A list of strings.
    
    Returns:
        list: The sorted list of strings.
    """
    def count_vowels(s):
        """Counts the number of vowels in a string, ignoring case and non-alphabetic characters."""
        return sum(1 for c in s.lower() if c in 'aeiou')

    return sorted(statements, key=count_vowels)
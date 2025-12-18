"""
QUESTION:
Write a function `sort_strings_by_vowels` that takes an array of strings as input and returns the array sorted in descending order of the number of vowels present in each string. If two strings have the same number of vowels, they should be sorted alphabetically.
"""

def sort_strings_by_vowels(strings):
    """
    Sorts an array of strings in descending order of the number of vowels present in each string.
    If two strings have the same number of vowels, they are sorted alphabetically.

    Args:
        strings (list): A list of strings.

    Returns:
        list: The sorted list of strings.
    """
    def count_vowels(string):
        """Counts the number of vowels in a string."""
        vowels = 'aeiouAEIOU'
        count = 0
        for char in string:
            if char in vowels:
                count += 1
        return count

    # Sort the array based on the number of vowels, followed by alphabetical order
    return sorted(strings, key=lambda x: (-count_vowels(x), x))
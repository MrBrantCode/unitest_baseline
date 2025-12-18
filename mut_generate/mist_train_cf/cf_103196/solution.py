"""
QUESTION:
Write a function named `filter_and_sort_strings` that filters a list of strings based on the presence of a specified character and returns the filtered list sorted in descending order by the frequency of the character in each string. If two or more strings have the same frequency, they should be sorted alphabetically. The function should take two parameters: `character` and `strings`.
"""

def filter_and_sort_strings(character, strings):
    """
    Filters a list of strings based on the presence of a specified character 
    and returns the filtered list sorted in descending order by the frequency 
    of the character in each string. If two or more strings have the same frequency, 
    they are sorted alphabetically.

    Args:
        character (str): The character to filter and sort by.
        strings (list): A list of strings.

    Returns:
        list: The filtered and sorted list of strings.
    """
    return sorted([string for string in strings if character in string], 
                  key=lambda x: (-x.count(character), x))
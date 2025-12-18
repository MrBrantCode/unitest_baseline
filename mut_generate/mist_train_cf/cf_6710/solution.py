"""
QUESTION:
Create a function `filter_and_sort_names` that takes a list of names as input. Select names that start with a vowel ('A', 'E', 'I', 'O', 'U') and have a length greater than 5. Sort the resulting list in descending order based on the number of vowels in the names. If multiple names have the same number of vowels, sort them alphabetically in descending order.
"""

def filter_and_sort_names(names):
    """
    This function filters a list of names to include only those starting with a vowel and having a length greater than 5.
    It then sorts the resulting list in descending order based on the number of vowels in the names.
    If multiple names have the same number of vowels, they are sorted alphabetically in descending order.

    Args:
        names (list): A list of names.

    Returns:
        list: The filtered and sorted list of names.
    """
    return sorted([name for name in names if name[0].lower() in ['a', 'e', 'i', 'o', 'u'] and len(name) > 5], 
                  key=lambda x: (sum(1 for char in x.lower() if char in ['a', 'e', 'i', 'o', 'u']), x.lower()), 
                  reverse=True)
"""
QUESTION:
Create a function named `filter_and_sort_dict` that takes a dictionary as input and returns a new dictionary containing only key-value pairs where the key starts with a vowel and the value is a list of integers. The keys in the new dictionary should be sorted alphabetically.
"""

def filter_and_sort_dict(dictionary):
    """
    Filters a dictionary to include only key-value pairs where the key starts with a vowel and the value is a list of integers.
    The keys in the new dictionary are sorted alphabetically.

    Args:
        dictionary (dict): The input dictionary to be filtered.

    Returns:
        dict: A new dictionary with the filtered key-value pairs.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_dict = {key: value for key, value in dictionary.items() 
                if key[0].lower() in vowels and isinstance(value, list) and all(isinstance(num, int) for num in value)}
    
    return dict(sorted(new_dict.items()))
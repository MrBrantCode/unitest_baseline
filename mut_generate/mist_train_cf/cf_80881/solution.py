"""
QUESTION:
Create a function `search_numbers` that takes a dictionary of numbers and a list of numbers to search for. Using dictionary's get() method and list comprehension, return a list of strings indicating which numbers from the search list are keys in the dictionary. If a number from the search list is not a key in the dictionary, it should not be included in the result. The function should handle exceptions when the dictionary key does not exist.
"""

def search_numbers(num_dict, search_list):
    """
    Searches for numbers in a dictionary and returns a list of strings indicating 
    which numbers from the search list are keys in the dictionary.

    Args:
        num_dict (dict): A dictionary of numbers.
        search_list (list): A list of numbers to search for.

    Returns:
        list: A list of strings indicating which numbers are keys in the dictionary.
    """
    return [f"{num} is in the dict" for num in search_list if num_dict.get(num, False)]
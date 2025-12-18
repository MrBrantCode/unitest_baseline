"""
QUESTION:
Create a function called `process_array` that takes an array of strings as input, removes any duplicates, filters out strings with less than 3 characters, creates a dictionary with the remaining strings as keys and their lengths as values, and returns the dictionary sorted by values in ascending order.
"""

def process_array(arr):
    """
    Removes duplicates from the input array, filters out strings with less than 3 characters,
    creates a dictionary with the remaining strings as keys and their lengths as values,
    and returns the dictionary sorted by values in ascending order.
    
    Args:
        arr (list): A list of strings.
    
    Returns:
        dict: A dictionary with strings as keys and their lengths as values, sorted by values in ascending order.
    """
    unique_arr = list(set(arr))  # Remove duplicates
    filtered_arr = [string for string in unique_arr if len(string) >= 3]  # Filter out strings with less than 3 characters
    dictionary = {string: len(string) for string in filtered_arr}  # Create a dictionary with strings as keys and their lengths as values
    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))  # Sort the dictionary by values in ascending order
    return sorted_dictionary
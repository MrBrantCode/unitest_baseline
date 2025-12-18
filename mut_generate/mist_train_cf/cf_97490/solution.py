"""
QUESTION:
Design a function named `search_string` that takes two parameters: an array of strings `arr` and a given string `given_str`. The function should search for `given_str` within the filtered array of strings that start with a capital letter, contain at least one vowel, and have a length of at least 5 characters. The function should be case sensitive and return the index of the first occurrence of `given_str` in the filtered array. If `given_str` is not found, return -1.
"""

def search_string(arr, given_str):
    """
    Searches for the given string within the filtered array of strings.
    
    The function filters the array to include only strings that start with a capital letter, 
    contain at least one vowel, and have a length of at least 5 characters. It then searches 
    for the given string within the filtered array and returns the index of the first occurrence. 
    If the given string is not found, it returns -1.
    
    Parameters:
    arr (list): The input array of strings.
    given_str (str): The string to be searched within the array.
    
    Returns:
    int: The index of the first occurrence of the given string in the filtered array, or -1 if not found.
    """
    filtered_arr = [string for string in arr if string[0].isupper() and any(char.lower() in 'aeiou' for char in string) and len(string) >= 5]
    for i in range(len(filtered_arr)):
        if filtered_arr[i] == given_str:
            return i
    return -1
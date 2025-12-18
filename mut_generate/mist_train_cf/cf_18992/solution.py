"""
QUESTION:
Write a function called "capitalize_array" that takes an array of strings as input, capitalizes the first letter of each word in each string, and returns the modified array. The function should not use any built-in Python functions or methods for capitalizing strings.
"""

def capitalize_array(A):
    """
    This function takes an array of strings as input, capitalizes the first letter of each word in each string, 
    and returns the modified array.

    Args:
        A (list): A list of strings

    Returns:
        list: A list of strings with the first letter of each word capitalized
    """

    capitalized_array = []
    for string in A:
        capitalized_string = ""
        for word in string.split():
            if len(word) > 0:
                capitalized_string += word[0].upper() + word[1:] + " "
            else:
                capitalized_string += " "
        capitalized_array.append(capitalized_string.strip())
    return capitalized_array
"""
QUESTION:
Function: Convert the given list of strings to a single string.

Description: Create a function that takes a list of strings as input, capitalizes each word, removes duplicates, filters out words with less than 3 characters, and sorts the remaining words in reverse alphabetical order. The resulting words should be combined into a single string without using the "join" method.

Restrictions: The resulting string should only contain words that are at least 3 characters long.
"""

def convert_string(str_list):
    """
    This function takes a list of strings, capitalizes each word, removes duplicates, 
    filters out words with less than 3 characters, and sorts the remaining words in 
    reverse alphabetical order. The resulting words are combined into a single string.

    Parameters:
    str_list (list): A list of strings.

    Returns:
    str: A single string containing the processed words.
    """

    # Remove duplicates by converting the list to a set
    unique_str_list = set(str_list)

    # Filter out words with less than 3 characters and capitalize each word
    filtered_str_list = [word.capitalize() for word in unique_str_list if len(word) >= 3]

    # Sort the remaining words in reverse alphabetical order
    sorted_str_list = sorted(filtered_str_list, reverse=True)

    # Combine the words into a single string without using the "join" method
    result_str = ''
    for word in sorted_str_list:
        result_str += word + ' '

    # Remove the trailing space at the end of the string
    result_str = result_str.strip()

    return result_str
"""
QUESTION:
Create a function `combine_palindromes` that combines two lists of strings, removes duplicates, and returns a new list containing only the palindrome strings. The function should take two lists of strings as input and return a list of strings. The order of the strings in the output list does not matter.
"""

def combine_palindromes(list1, list2):
    """
    Combines two lists of strings, removes duplicates, and returns a new list containing only the palindrome strings.

    Args:
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        list: A list of palindrome strings.
    """
    combined_list = list1 + list2  # Combine both lists
    result_list = []

    # Check each string in the combined list
    for string in combined_list:
        if string == string[::-1]:  # Check if the string is a palindrome
            if string not in result_list:  # Check if the string is not already in the result list
                result_list.append(string)  # Add the palindrome string to the result list

    return result_list
"""
QUESTION:
Combine two lists of strings into one list without duplicates, and include only the strings that are palindromes. The function should be named `combine_palindromes`. The function should take two lists of strings as input and return a list of strings. The list should not contain duplicate strings.
"""

def combine_palindromes(list1, list2):
    """
    Combines two lists of strings into one list without duplicates, 
    and includes only the strings that are palindromes.

    Args:
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        list: A list of strings that are palindromes, without duplicates.
    """
    combined_list = list1 + list2
    result_list = []

    # Check each string in the combined list
    for string in combined_list:
        if string == string[::-1]:  # Check if the string is a palindrome
            if string not in result_list:  # Check if the string is not already in the result list
                result_list.append(string)  # Add the palindrome string to the result list

    return result_list
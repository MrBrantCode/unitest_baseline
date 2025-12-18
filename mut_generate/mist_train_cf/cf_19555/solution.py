"""
QUESTION:
Write a function `replace_and_count` that takes a string of up to 10^6 characters as input and returns the modified string with all instances of 'e' replaced with 'X' and the count of 'e' occurrences. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def replace_and_count(string):
    """
    Replaces all instances of 'e' with 'X' in the input string and returns the modified string along with the count of 'e' occurrences.

    Args:
    string (str): The input string of up to 10^6 characters.

    Returns:
    tuple: A tuple containing the modified string and the count of 'e' occurrences.
    """
    count = 0
    result = ''
    for char in string:
        if char == 'e':
            count += 1
            result += 'X'
        else:
            result += char
    return result, count
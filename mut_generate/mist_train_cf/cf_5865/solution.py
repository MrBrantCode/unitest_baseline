"""
QUESTION:
Write a function `concatenate_strings` that takes two string arguments and returns their concatenation without using the `+` operator or any built-in string concatenation methods. The function should be efficient with a time complexity of O(n), where n is the total length of the input strings.
"""

def concatenate_strings(str1, str2):
    """
    Concatenates two input strings without using the '+' operator or built-in string concatenation methods.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated string.
    """
    output = list(str1)
    for char in str2:
        output.append(char)
    return ''.join(output)
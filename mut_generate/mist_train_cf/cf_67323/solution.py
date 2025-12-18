"""
QUESTION:
Design a recursive function named `reverse_string` that takes a string as input and returns the reversed string. The function should be able to handle strings of varying lengths. Note that this recursive function may not be efficient for very large strings due to Python's recursion limit.
"""

def reverse_string(input_string, index=0):
    """
    A recursive function that takes a string as input and returns the reversed string.

    Args:
        input_string (str): The input string to be reversed.
        index (int, optional): The current index in the recursion. Defaults to 0.

    Returns:
        str: The reversed input string.
    """
    if input_string == "":
        return input_string
    elif index == len(input_string):
        return ""
    else:
        return reverse_string(input_string, index + 1) + input_string[index]
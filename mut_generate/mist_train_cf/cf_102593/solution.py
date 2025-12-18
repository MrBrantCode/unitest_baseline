"""
QUESTION:
Write a function called `replace_and_count` that takes an input string and replaces all occurrences of the letter "o" with the letter "e" and returns the modified string along with the total count of the letter "l" in the original string.
"""

def replace_and_count(input_string):
    """
    Replaces all occurrences of 'o' with 'e' in the input string and returns the modified string along with the total count of 'l' in the original string.

    Args:
        input_string (str): The input string to be modified.

    Returns:
        tuple: A tuple containing the modified string and the count of 'l' in the original string.
    """
    new_string = input_string.replace("o", "e")
    count_l = input_string.count("l")
    return new_string, count_l
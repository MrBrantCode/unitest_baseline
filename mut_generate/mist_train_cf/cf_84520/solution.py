"""
QUESTION:
Create a function `count_chars` that takes a string as input and returns the counts of alphabetical letters, numerical digits, special characters, and uppercase letters. The function should have a space complexity of O(1). If the string contains at least one numerical digit, one alphabetical letter, one special character, and one uppercase letter, return the counts separately; otherwise, return a respective message.
"""

def count_chars(string):
    """
    Counts the number of alphabetical letters, numerical digits, special characters, and uppercase letters in a string.

    Args:
        string (str): The input string.

    Returns:
        tuple: A tuple containing the counts of alphabetical letters, numerical digits, special characters, and uppercase letters.
        str: A message if the string does not contain at least one numerical digit, one alphabetical letter, one special character, and one uppercase letter.
    """
    alpha = 0
    num = 0
    special = 0
    upper = 0

    for ch in string:
        if ch.isalpha():
            alpha += 1
            if ch.isupper():
                upper += 1
        elif ch.isdigit():
            num += 1
        else:
            special += 1

    if alpha > 0 and num > 0 and special > 0 and upper > 0:
        return alpha, num, special, upper
    else:
        return "The string does not contain at least one numerical digit, one alphabetical letter, one special character, and one uppercase letter."
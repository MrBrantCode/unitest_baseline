"""
QUESTION:
Write a function `is_valid_isbn` to determine if a given string is a valid ISBN-10 number. The input string can have a maximum length of 20 characters, consisting of alphanumeric characters, hyphens, and spaces, and can be separated by hyphens or spaces. The function should consider strings with or without hyphens or spaces as valid ISBN-10 numbers. The check digit must be valid, i.e., it must satisfy the ISBN-10 check digit calculation.
"""

def is_valid_isbn(isbn):
    """
    This function checks if a given string is a valid ISBN-10 number.
    
    Args:
        isbn (str): The input string to be checked.
    
    Returns:
        bool: True if the string is a valid ISBN-10 number, False otherwise.
    """
    
    # Remove hyphens and spaces from the string
    isbn = isbn.replace("-", "").replace(" ", "")

    # Check if the string has a length of 10 characters
    if len(isbn) != 10:
        return False

    # Initialize the sum of the weighted digits
    weighted_sum = 0

    # Check the first 9 characters
    for i in range(9):
        # Check if the character is a digit
        if not isbn[i].isdigit():
            return False
        # Calculate the weighted sum
        weighted_sum += (10 - i) * int(isbn[i])

    # Check the last character (check digit)
    if isbn[9].upper() == "X":
        # Check digit is 'X'
        weighted_sum += 10
    elif not isbn[9].isdigit():
        # Check digit is not a digit
        return False
    else:
        # Check digit is a digit
        weighted_sum += int(isbn[9])

    # Check if the weighted sum is divisible by 11
    return weighted_sum % 11 == 0
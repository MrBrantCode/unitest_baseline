"""
QUESTION:
Create a function `highest_palindrome` that takes two integers `low` and `high` as input, representing an integer range. The function should return the highest palindrome number within the range. If no palindrome is found, it should return 0.
"""

def highest_palindrome(low, high):
    """Returns highest palindrome integer within the given range, 
    zero if no palindrome found.
    """

    # Start from highest point and go backwards to the lower limit
    for i in range(high, low - 1, -1):
        # Check if the number is a palindrome
        if str(i) == str(i)[::-1]:
            return i
    return 0
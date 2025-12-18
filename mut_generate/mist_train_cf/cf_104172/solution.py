"""
QUESTION:
Create a function called `check_number` that takes an integer as input. The function should use an if-else statement to categorize the number into one of four categories based on whether it is negative or positive and whether it is divisible by 3. The function should return a string indicating the category of the number: "Negative and divisible by 3", "Negative but not divisible by 3", "Positive and divisible by 3", or "Positive but not divisible by 3".
"""

def check_number(num):
    """
    Categorize an integer into one of four categories based on whether it is negative or positive and whether it is divisible by 3.

    Args:
        num (int): The input integer.

    Returns:
        str: A string indicating the category of the number.
    """
    if num < 0:
        if num % 3 == 0:
            return "Negative and divisible by 3"
        else:
            return "Negative but not divisible by 3"
    else:
        if num % 3 == 0:
            return "Positive and divisible by 3"
        else:
            return "Positive but not divisible by 3"
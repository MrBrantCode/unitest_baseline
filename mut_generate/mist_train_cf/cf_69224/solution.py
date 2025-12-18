"""
QUESTION:
Create a function called `find_second_biggest` that takes a list of numbers as input and returns the second biggest number. The function should assume that the input list contains at least two different numbers. If all numbers in the list are the same, the function may return the initialized value (negative infinity or any number smaller than the smallest possible input number) as the second biggest number is undefined in this case.
"""

def find_second_biggest(numbers):
    """
    This function finds the second biggest number in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        The second biggest number in the list. If all numbers in the list are the same, returns negative infinity.
    """

    # Initialize max1 and max2 as negative infinity
    max1 = max2 = float('-inf')

    # Iterate through the list of numbers
    for n in numbers:
        # If n is greater than max1, set max2 to be equal to max1 and replace max1 with n
        if n > max1:
            max2 = max1
            max1 = n
        # If n is not greater than max1 and n is greater than max2, then replace max2 with n
        elif n > max2 and n != max1:
            max2 = n

    # Return max2 as the second biggest number
    return max2
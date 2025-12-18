"""
QUESTION:
Write a function named `mean_positive_even_greater_than_four` that calculates the mean of all the positive even numbers greater than 4 in a given list of integers. The function should return the mean as a float. If the list does not contain any positive even numbers greater than 4, the function should return 0.
"""

def mean_positive_even_greater_than_four(arr):
    """
    This function calculates the mean of all the positive even numbers greater than 4 in a given list of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        float: The mean of all the positive even numbers greater than 4 in the list. If the list does not contain any positive even numbers greater than 4, it returns 0.
    """
    # Filter the list to include only positive even numbers greater than 4
    positive_even_numbers = [num for num in arr if num > 4 and num % 2 == 0]
    
    # If the list is not empty, calculate the mean
    if positive_even_numbers:
        # Calculate the sum of the numbers and divide by the count
        mean = sum(positive_even_numbers) / len(positive_even_numbers)
    else:
        # If the list is empty, return 0
        mean = 0
    
    return mean
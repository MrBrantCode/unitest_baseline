"""
QUESTION:
Write a function named `sum_even_numbers` that calculates the sum of all even numbers in a given array and returns the result. The function should iterate through each element in the array, check if the element is even by verifying if it is divisible by 2 with no remainder, and add it to the sum if it is even.
"""

def sum_even_numbers(arr):
    """
    This function calculates the sum of all even numbers in a given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of all even numbers in the array.
    """
    sum = 0
    for num in arr:
        if num % 2 == 0:
            sum += num
    return sum
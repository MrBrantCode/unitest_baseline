"""
QUESTION:
Create a function named `sum_odd_numbers` that calculates the sum of all odd numbers within a specified range (inclusive) using a while loop. The function should take two parameters, `start` and `end`, representing the start and end of the range, respectively. The function should not include any print statements or return any specific messages, only the sum of the odd numbers.
"""

def sum_odd_numbers(start, end):
    """
    Calculate the sum of all odd numbers within a specified range (inclusive).

    Parameters:
    start (int): The start of the range.
    end (int): The end of the range.

    Returns:
    int: The sum of all odd numbers in the range.
    """
    num = start
    sum_odd = 0
    while num <= end:
        if num % 2 != 0:  
            sum_odd += num  
        num += 1  
    return sum_odd
"""
QUESTION:
Create a function called `calculate_sum` that calculates the sum of all the values in a given array that are divisible by 3 and less than 10. If a value is greater than or equal to 10, the function should print a warning message and skip adding it to the sum.
"""

def calculate_sum(arr):
    """
    Calculate the sum of all the values in a given array that are divisible by 3 and less than 10.
    If a value is greater than or equal to 10, print a warning message and skip adding it to the sum.

    Parameters:
    arr (list): The input list of numbers.

    Returns:
    int: The sum of the numbers in the list that are divisible by 3 and less than 10.
    """
    total_sum = 0
    for num in arr:
        if num >= 10:
            print("Warning: Skipping value", num)
            continue
        if num % 3 == 0:
            total_sum += num
    return total_sum
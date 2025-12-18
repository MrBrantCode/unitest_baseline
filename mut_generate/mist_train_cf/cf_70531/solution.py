"""
QUESTION:
Create a function named `SumOfOddNumbers` that takes an integer `n` as input and returns the sum of odd integers from 1 to `n`. If the input `n` is not a valid integer, set `n` to 100 and proceed with the calculation. Implement exception handling to prevent system crashes and display an error message for invalid inputs.
"""

def sum_of_odd_numbers(n):
    """
    This function calculates the sum of odd integers from 1 to n.
    If the input n is not a valid integer, it defaults to 100.

    Args:
        n (int): The upper limit for the sum of odd integers.

    Returns:
        int: The sum of odd integers from 1 to n.
    """
    try:
        n = int(n)
    except ValueError:
        print("Your input was not valid. Proceeding with sum of integers from 1 to 100 instead.")
        n = 100

    sum_of_odd = sum(i for i in range(1, n+1) if i % 2 != 0)
    return sum_of_odd
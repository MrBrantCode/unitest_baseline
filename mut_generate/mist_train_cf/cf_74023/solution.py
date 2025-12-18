"""
QUESTION:
Create a function `lucas_series(n)` that returns the nth Lucas number in the series, where the Lucas series is defined as: L(0) = 2, L(1) = 1, and for n > 1, L(n) = L(n-1) + L(n-2). Use this function to generate the first 15 numbers in the Lucas series. The function should be efficient and avoid repeated calculations.
"""

def lucas_series(n):
    """
    Calculate the nth Lucas number.

    Args:
    n (int): The index of the Lucas number to calculate.

    Returns:
    int: The nth Lucas number.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas_numbers = [2, 1] # starting values
        # calculate the rest
        for _ in range(2, n + 1):  
            lucas_numbers.append(sum(lucas_numbers[-2:]))
        return lucas_numbers[n]
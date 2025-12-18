"""
QUESTION:
Write a function named `sum_odd_integers` that calculates the sum of all odd integers between two given integers `n1` and `n2` (inclusive), excluding any number that is divisible by 3. Assume `n1` is the smaller integer and `n2` is the larger integer.
"""

def sum_odd_integers(n1, n2):
    """
    Calculate the sum of all odd integers between two given integers n1 and n2 (inclusive),
    excluding any number that is divisible by 3.

    Args:
        n1 (int): The smaller integer.
        n2 (int): The larger integer.

    Returns:
        int: The sum of the odd integers.
    """
    # Determine the smallest odd integer greater than or equal to n1
    start = n1 if n1 % 2 != 0 else n1 + 1
    
    # Determine the largest odd integer less than or equal to n2
    end = n2 if n2 % 2 != 0 else n2 - 1
    
    # Calculate the sum of the odd integers excluding numbers divisible by 3
    total = sum(num for num in range(start, end + 1, 2) if num % 3 != 0)
    
    return total
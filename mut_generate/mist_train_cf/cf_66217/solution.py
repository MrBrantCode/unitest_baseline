"""
QUESTION:
Create a function called `fizz_buzz(n)` that calculates the total occurrence of the digit 7 in integers less than 'n' that are divisible by either 11 or 13, but not both simultaneously. The function should be able to handle large data ranges, potentially as high as 10^9, efficiently.
"""

def fizz_buzz(n):
    """
    Calculate the total occurrence of the digit 7 in integers less than 'n' 
    that are divisible by either 11 or 13, but not both simultaneously.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The total occurrence of the digit 7.
    """
    def count_sevens(k, m):
        # Calculate the number of multiples of m less than k
        count = k // m
        # Calculate the number of multiples of m that have 7 in the units place
        sevens = count // 10 + (1 if count % 10 >= 7 else 0)
        return sevens

    # Calculate the total occurrence of the digit 7
    total_sevens = 0
    total_sevens += count_sevens(n, 11) + count_sevens(n, 13)
    total_sevens -= count_sevens(n, 11 * 13) * 2  # Subtract the overlap
    return total_sevens
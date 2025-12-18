"""
QUESTION:
Find the number of palindromic numbers among the integers between A and B (inclusive).
Here, a palindromic number is a positive integer whose string representation in base 10 (without leading zeros) reads the same forward and backward.

-----Constraints-----
 - 10000 \leq A \leq B \leq 99999
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the number of palindromic numbers among the integers between A and B (inclusive).

-----Sample Input-----
11009 11332

-----Sample Output-----
4

There are four integers that satisfy the conditions: 11011, 11111, 11211 and 11311.
"""

def count_palindromic_numbers(A: int, B: int) -> int:
    """
    Counts the number of palindromic numbers between A and B (inclusive).

    Parameters:
    - A (int): The lower bound of the range (inclusive).
    - B (int): The upper bound of the range (inclusive).

    Returns:
    - int: The number of palindromic numbers between A and B (inclusive).
    """
    def is_palindromic(num: int) -> bool:
        """Helper function to check if a number is palindromic."""
        s = str(num)
        return s == s[::-1]
    
    count = 0
    for i in range(A, B + 1):
        if is_palindromic(i):
            count += 1
    
    return count
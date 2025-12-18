"""
QUESTION:
The Little Elephant loves numbers. 

He has a positive integer x. The Little Elephant wants to find the number of positive integers d, such that d is the divisor of x, and x and d have at least one common (the same) digit in their decimal representations. 

Help the Little Elephant to find the described number.

Input

A single line contains a single integer x (1 ≤ x ≤ 109).

Output

In a single line print an integer — the answer to the problem.

Examples

Input

1


Output

1


Input

10


Output

2
"""

from math import sqrt

def check(n, d):
    """Helper function to check if two numbers have at least one common digit."""
    n = str(n)
    d = str(d)
    for c in d:
        if c in n:
            return True
    return False

def get_divisors(n):
    """Helper function to get all divisors of a number."""
    m = int(sqrt(n)) + 1
    divisors = set()
    for d in range(1, m):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return list(divisors)

def count_common_digit_divisors(x):
    """
    Function to count the number of divisors of x that have at least one common digit with x.
    
    Parameters:
    x (int): The number for which we need to find the divisors with common digits.
    
    Returns:
    int: The count of such divisors.
    """
    divs = get_divisors(x)
    count = 0
    for d in divs:
        if check(x, d):
            count += 1
    return count
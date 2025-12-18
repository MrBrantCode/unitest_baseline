"""
QUESTION:
Write a program which reads an integer n and prints the factorial of n. You can assume that n ≤ 20.



Input

An integer n (1 ≤ n ≤ 20) in a line.

Output

Print the factorial of n in a line.

Example

Input

5


Output

120
"""

def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a given integer n.

    Parameters:
    n (int): The integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the integer n.
    """
    if n < 0 or n > 20:
        raise ValueError("Input must be an integer between 1 and 20 inclusive.")
    
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    
    return ans
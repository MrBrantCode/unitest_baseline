"""
QUESTION:
A triangular number is the number of dots in an equilateral triangle uniformly filled with dots. For example, three dots can be arranged in a triangle; thus three is a triangular number. The n-th triangular number is the number of dots in a triangle with n dots on a side. <image>. You can learn more about these numbers from Wikipedia (http://en.wikipedia.org/wiki/Triangular_number).

Your task is to find out if a given integer is a triangular number.

Input

The first line contains the single number n (1 ≤ n ≤ 500) — the given integer.

Output

If the given integer is a triangular number output YES, otherwise output NO.

Examples

Input

1


Output

YES


Input

2


Output

NO


Input

3


Output

YES
"""

def is_triangular_number(n: int) -> str:
    """
    Determines if a given integer is a triangular number.

    Parameters:
    n (int): The integer to be checked.

    Returns:
    str: "YES" if n is a triangular number, otherwise "NO".
    """
    if n < 1 or n > 500:
        raise ValueError("The input number must be between 1 and 500.")
    
    triangular_numbers = [i * (i + 1) // 2 for i in range(1, 32)]
    
    return "YES" if n in triangular_numbers else "NO"
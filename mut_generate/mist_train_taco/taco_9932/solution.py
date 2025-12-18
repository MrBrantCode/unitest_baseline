"""
QUESTION:
Find sum of all the numbers that are multiples of 10 and are less than or equal to a given number "N". (quotes for clarity and be careful of integer overflow)

-----Input-----
Input will start with an integer T the count of test cases, each case will have an integer N.

-----Output-----
Output each values, on a newline.

-----Constraints-----
- 1 ≤ T ≤ 10
- 1 ≤ N ≤1000000000

-----Example-----
Input:
1
10

Output:
10

-----Explanation-----
Example case 1. Only integer that is multiple 10 that is less than or equal to 10 is 10
"""

def sum_multiples_of_10(N: int) -> int:
    """
    Calculate the sum of all multiples of 10 that are less than or equal to N.

    Parameters:
    N (int): The upper limit for finding multiples of 10.

    Returns:
    int: The sum of all multiples of 10 less than or equal to N.
    """
    N -= N % 10
    N //= 10  # Use integer division to avoid floating-point issues
    return N * (N + 1) // 2 * 10  # Use integer division to avoid floating-point issues
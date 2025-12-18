"""
QUESTION:
Given an integer N. You have to find the number of digits that appear in its factorial, where factorial is defined as, factorial(N) = 1*2*3*4..*N and factorial(0) = 1.
 
Example 1:
Input:
N = 5
Output:
3
Explanation:
5! is 120 so there are 3
digits in 120
Example 2:
Input:
N = 10
Output:
7
Explanation:
10! is 3628800 so there are
7 digits in 3628800
Your Task: 
You don't need to read input or print anything. Your task is to complete the function facDigits() which takes an integer N as input parameter and returns the number of digits in factorial of N.
 
Expected Time Complexity: O(Log(N))
Expected Space Complexity: O(1)
 
Constraints:
1 ≤ N ≤ 10^{4}
"""

import math

def count_digits_in_factorial(N: int) -> int:
    """
    Calculate the number of digits in the factorial of a given integer N.

    Parameters:
    N (int): The integer for which the factorial is to be calculated.

    Returns:
    int: The number of digits in the factorial of N.
    """
    return len(str(math.factorial(N)))
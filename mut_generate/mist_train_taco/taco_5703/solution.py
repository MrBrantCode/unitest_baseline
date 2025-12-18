"""
QUESTION:
Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2^{x} for some x.
Example 1:
Input: N = 1
Output: YES
Explanation:1 is equal to 2 
raised to 0 (2^{0} = 1).
Example 2:
Input: N = 98
Output: NO
Explanation: 98 cannot be obtained
by any power of 2.
Your Task:Your task is to complete the function isPowerofTwo() which takes n as a parameter and returns true or false by checking if the given number can be represented as a power of two or not.
Expected Time Complexity:O(log N).
Expected Auxiliary Space:O(1).
Constraints:
0 ≤N ≤10^{18}
"""

def is_power_of_two(n: int) -> bool:
    """
    Check if the given non-negative integer n is a power of 2.

    Parameters:
    n (int): The number to be checked.

    Returns:
    bool: True if n is a power of 2, False otherwise.
    """
    if n <= 0:
        return False
    return n & (n - 1) == 0
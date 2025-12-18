"""
QUESTION:
Given a natural number N, find the number of ways in which N can be expressed as a sum of natural numbers when order is taken into consideration. Two sequences that differ in the order of their terms define different compositions of their sum.
 
Example 1:
Input: N = 2
Output: 2
Explanation: All 2 compositions are 
{1 + 1} and {2}.
Example 2:
Input: N = 4
Output: 8
Explanation: All 8 compositions are:
{1 + 1 + 1 + 1}, {1 + 1 + 2}, {1 + 2 + 1},
{2 + 1 + 1}, {2 + 2}, {1 + 3}, {3 + 1}, {4}.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function no_of_ways() which takes n as the input parameter and returns the total no. of ways modulo 10^{9} + 7.
 
Expected Time Complexity: O(log(N))
Expected Space Complexity: O(1)
Constraints:
1 <= N <= 10^{9}
"""

def count_compositions(n: int) -> int:
    """
    Counts the number of ways in which a natural number N can be expressed as a sum of natural numbers,
    considering the order of terms.

    Parameters:
    n (int): The natural number N.

    Returns:
    int: The number of compositions modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    return pow(2, n - 1, MOD)
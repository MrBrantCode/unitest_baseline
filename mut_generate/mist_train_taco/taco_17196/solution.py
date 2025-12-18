"""
QUESTION:
Given a series of numbers 0  1  4  18  96  600  4320 …., and series starting from zeroth term. Given n, find the nth value of the series.
 
Example 1:
Input: n = 4
Output: 96
Example 2:
Input: n = 2
Output: 4
 
Your Task:
You don't need to read or print anything, Your task is to complete the function NthTerm() which takes n as input parameter and returns the nth value of the given series modulo 10^{9} + 7.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
Constraints:
1 <= n <= 10000
"""

def nth_term(n: int) -> int:
    """
    Calculate the nth term of the series modulo 10^9 + 7.

    The series is defined as:
    - 0th term: 0
    - 1st term: 1
    - 2nd term: 4
    - 3rd term: 18
    - 4th term: 96
    - ...

    The nth term is given by n * (n!) % (10^9 + 7).

    Parameters:
    - n (int): The position in the series for which to calculate the value.

    Returns:
    - int: The nth value of the series modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    
    # Calculate n!
    factorial = 1
    for i in range(1, n + 1):
        factorial = (factorial * i) % MOD
    
    # Calculate n * (n!) % (10^9 + 7)
    result = (n * factorial) % MOD
    
    return result
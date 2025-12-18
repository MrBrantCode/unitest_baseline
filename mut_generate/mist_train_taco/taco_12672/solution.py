"""
QUESTION:
Given a number n, find the last non-zero digit in n!.
Examples:
Input  : n = 5
Output : 2
5! = 5 * 4 * 3 * 2 * 1 = 120
Last non-zero digit in 120 is 2.
Input  : n = 33
Output : 8
Your Task:  
You don't need to read input or print anything. Your task is to complete the function lastNon0Digit() which takes the integer N as input parameters and returns the last non-zero digit in n!.
Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 100
"""

def last_non_zero_digit(n: int) -> int:
    def factorial_with_last_non_zero(N):
        if N == 1:
            return 1
        result = N * factorial_with_last_non_zero(N - 1)
        while result % 10 == 0:
            result //= 10
        return result % 100000  # To avoid large number issues, keep only the last 5 digits

    factorial_result = factorial_with_last_non_zero(n)
    while factorial_result % 10 == 0:
        factorial_result //= 10
    return factorial_result % 10
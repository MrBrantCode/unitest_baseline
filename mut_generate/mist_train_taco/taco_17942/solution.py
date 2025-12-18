"""
QUESTION:
Given a number n, find the total numbers, less than or equal to n which have at-least one common factor with n other than 1.
 
Example 1:
Input: n = 6
Output: 4
Explanation: For n=6, the 4 numbers having 
a common factor between them and 6 
are : 2, 3, 4 & 6
Example 2:
Input: n = 15
Output: 7
Explanation: For N=15, the 7 numbers having a 
common factor between them and 15 
are : 3, 5, 6, 9, 10, 12, 15
 
Your Task:
You don't need to read or print anything. Your task is to complete the function CommonFactor() which takes n as input parameter and returns total numbers. less than or equal to n which have atleast one common factor with n other than 1.
 
Expected Time Complexity: O(nlog(n))
Expected Space Complexity: O(n)
Constraints:
1 <= n <= 10^{5}
"""

def count_numbers_with_common_factors(n: int) -> int:
    sieve = [True] * (n + 1)
    res = [False] * (n + 1)
    for i in range(2, n + 1):
        if sieve[i]:
            can = n % i == 0
            for j in range(i, n + 1, i):
                sieve[j] = False
                res[j] |= can
    return sum(res)
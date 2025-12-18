"""
QUESTION:
Given a number N. Find the minimum number of squares of any number that sums to N. For Example: If N = 100 , N can be expressed as (10*10) and also as (5*5 + 5*5 + 5*5 + 5*5) but the output will be 1 as minimum number of square is 1 , i.e (10*10).
 
Example 1:
Input: N = 100
Output: 1
Explanation: 10 * 10 = 100
Example 2:
Input: N = 6
Output: 3
Explanation = 1 * 1 + 1 * 1 + 2 * 2 = 6
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function MinSquares() which takes N as input parameter and returns minimum number of squares needed to make N.
 
Expcted Time Complexity: O(N * sqrt(N) )
Expected Space Complexity: O(N)
 
Constraints:
1 <= N <= 10000
"""

from math import sqrt, ceil

def min_squares(n: int) -> int:
    if n < 0:
        return -1
    if n <= 3:
        return n
    
    # Initialize a list to store the minimum number of squares for each number up to n
    F = [-1] * (n + 1)
    
    # Base cases
    F[0] = 0
    F[1] = 1
    F[2] = 2
    F[3] = 3
    
    # Fill the list using dynamic programming
    for i in range(4, n + 1):
        F[i] = i  # Initialize with the worst case (all 1s)
        for x in range(1, int(sqrt(i)) + 1):
            temp = x * x
            if temp > i:
                break
            F[i] = min(F[i], 1 + F[i - temp])
    
    return F[n]
"""
QUESTION:
Given a series as shown below:
               1  2
            3  4  5  6
        7  8  9 10 11 12
 13 14 15 16 17 18 19 20
    ..........................
    ............................
             (so on)
Find the sum of Nth row.
 
Example 1:
Input: N = 2
Output: 18
Explanation: Sum of 2nd row is 3 + 4 + 
5 + 6 = 18.
Example 2:
Input: N = 4
Output: 132
Explanation: Sum of 4th row is 132.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Nth_rowSum() which takes N as input parameter and returns sum of Nth row modulo 10^{9}  + 7.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{4}
"""

def Nth_rowSum(n: int) -> int:
    m = 10**9 + 7
    return (2 * n * n + 1) * n % m
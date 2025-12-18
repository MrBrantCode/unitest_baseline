"""
QUESTION:
Given a positive integer n. Find the sum of product of x and y such that floor(n/x) = y .
 
Example 1:
Input: n = 5
Output: 21
Explanation: Following are the possible 
pairs of (x, y):
(1, 5), (2, 2), (3, 1), (4, 1), (5, 1).
So, 1*5 + 2*2 + 3*1 + 4*1 + 5*1 
   = 5 + 4 + 3 + 4 + 5 
   = 21.
Example 2:
Input: n = 10
Output: 87
Explanation: Sum of product of all 
possible pairs of (x, y) is 87.
 
Your Task:
You don't need to read or print anything. Your task is to cpmplete the function sumofproduct() which takes n as input parameter and returns the sum of product of all possible pairs(x, y).
 
Expected Time Complexity: O(n)
Expected Space Compelxity: O(1)
 
Constraints:
1 <= n <= 10^{6}
"""

def sum_of_product(n: int) -> int:
    sum_product = 0
    for x in range(1, n + 1):
        y = n // x
        sum_product += x * y
    return sum_product
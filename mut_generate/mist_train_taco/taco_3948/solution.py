"""
QUESTION:
Given two integers L and R . Find the resultant after applying the series of Bitwise AND ( & ) operation on every natural number between the Range L and R (including both).
 
Example 1:
Input: L = 8, R = 13
Output: 8
Explanation: 
8 AND 9 AND 10 AND 11 AND 12 AND 13 = 8.
Example 2:
Input: L = 2, R = 3
Output: 2
Explanation: 2 AND 3 = 2.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function find_and() which takes l and r as input parameter and returns AND operation on every number between l to r.
 
Expected Time Complexity: O(log(n))
Expected Time Complexity: O(1)
 
Constraints:
1 <= L<= R < =10^{8}
"""

def find_and(l: int, r: int) -> int:
    while r > l:
        r &= r - 1
    return r & l
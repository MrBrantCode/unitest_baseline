"""
QUESTION:
Given a number N, print all the composite numbers less than or equal to N. The number should be printed in ascending order.
Example 1:
Input: N = 10
Output: 4, 6, 8, 9, 10
Explaination: From 1 to 10 these are 
the only composite numbers.
Example 2:
Input: N = 6
Output: 4, 6
Explaination: From 1 to 6 these are 
the only composite numbers.
Your Task:
You do not need to read input or print anything. Your task is to complete the function compositeNumbers() which takes N as input parameters and returns a list containing all the composite numbers from 1 to N.
Expected Time Complexity: O(N* sqrt(N))
Expected Auxiliary Space: O(N)
Constraints:
4 ≤ N ≤ 10^{4}
"""

import math

def find_composite_numbers(N):
    def composites(n):
        pl = [True] * (n + 1)
        pl[0] = pl[1] = False
        lim = int(math.sqrt(n)) + 1
        for i in range(2, lim):
            if pl[i]:
                for j in range(i * i, n + 1, i):
                    pl[j] = False
        res = []
        for i in range(2, n + 1):
            if not pl[i]:
                res.append(i)
        return res
    return composites(N)
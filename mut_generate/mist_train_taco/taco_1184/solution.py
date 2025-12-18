"""
QUESTION:
Given Two integers L and R find the total number of distinct pairs (p,q)  between L and R ( both inclusive ) satisfying the given relationship. p! * q!=k^2 (a perfect square) where p,q,k is any integer and '!' denotes factorial.
Example 1:
Input: L = 0, R = 1
Output: 1
Explanation: 1 is the only perfect square
between 0 and 1; 
Example 2:
Input: L = 9, R = 25
Output: 3
Explanation: 9, 16 and 25 are the perfect 
squares between 9 and 25. 
Your Task:  
You don't need to read input or print anything. Complete the function countPerfectSquares() which takes L and R as an input parameter and returns the total number of perfect squares.
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
0<= L <= R <=10^{18}
"""

import math

def is_perfect_square(x):
    if x >= 0:
        sr = math.floor(math.sqrt(x))
        return sr * sr == x
    return False

def count_perfect_squares(L, R):
    if is_perfect_square(L):
        return math.floor(math.sqrt(R)) - math.floor(math.sqrt(L)) + 1
    else:
        return math.floor(math.sqrt(R)) - math.floor(math.sqrt(L))
"""
QUESTION:
Given a rectangle of size L x B. Find the minimum number of squares required to fill the rectangle such that no two square overlaps.
Example 1:
Input: L = 4, B = 5
Output: 5
Explaination: One 4*4 square and four 1*1 
squares are required.
Example 2:
Input: L = 2, B = 4
Output: 2
Explaintion: Two 2*2 squares are enough to 
fill the rectangle.
Your Task:
You do not need to read input or print anything. Your task is to complete the  function minSquares() which takes L and B as input parameters and returns minimum number of squares required to fill the rectangle. Return the answer modulo 10^{9} + 7.
Expected Time Complexity: O(log(max(L, B)))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ L, B ≤ 10^{10}
"""

def min_squares(L: int, B: int) -> int:
    p = 1000000007
    
    if L == 1:
        return B % p
    if B == 1:
        return L % p
    
    ans = 0
    while L > 0 and B > 0:
        if L > B:
            ans = (ans + L // B) % p
            L = L % B
        else:
            ans = (ans + B // L) % p
            B = B % L
    
    return ans % p
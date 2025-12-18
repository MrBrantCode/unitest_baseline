"""
QUESTION:
Given 2 integers N and K. Convert N(given in Decimal) to base K.
 
Example 1:
Input:
N = 10, K = 2
Output:
1010
Explanation:
(10)_{10} = (1010)_{2}
Example 2:
Input:
N = 4, K = 8
Output:
4
Explanation:
(4)_{10} = (4)_{8}
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function changeBase() which takes Integers N and K as input and returns an integer as the answer.
 
Expected Time Complexity: O(log_{K}N)
Expected Auxiliary Space: O(log_{K}N)
 
Constraints:
1 <= N <= 10^{5}
2 <= K <= 10
"""

def convert_to_base(N: int, K: int) -> int:
    from collections import deque
    result = deque()
    while N:
        result.appendleft(str(N % K))
        N //= K
    return int(''.join(result))
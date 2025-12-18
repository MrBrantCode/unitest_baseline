"""
QUESTION:
Given a number N, find the sum of all its factors.
Example 1:
Input: N = 30
Output: 72
Explanation: Factors sum 1 + 2 + 3 + 5 
+ 6 + 10 + 15 + 30 = 72
Example 2:
Input: N = 15
Output: 24
Explanation: Factors sum 1 + 3 + 5 
+ 15 = 24
Your Task:  
You don't need to read input or print anything. Your task is to complete the function factorSum() which takes N as input and returns the sum.
Expected Time Complexity: O(sqrt N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{9}
"""

def calculate_factor_sum(N: int) -> int:
    if N == 1:
        return 1
    if N == 0:
        return 0
    
    factors = [1, N]
    i = 2
    while i < int(N ** 0.5) + 1:
        if N % i == 0:
            factors.append(i)
            if i != N // i:
                factors.append(N // i)
        i += 1
    
    return sum(factors)
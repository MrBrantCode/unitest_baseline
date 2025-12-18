"""
QUESTION:
You are given a integer N and another integer K. You have to find how many integers (n) are possible such that N is the integeral part of Kth root of the integer (n).
Example 1:
Input: N = 3, K = 2
Output: 7
Explaination: 9, 10, 11, 12, 13, 14, 15 
have 3 as integral part of there square root.
Example 2:
Input: N = 2, K = 3
Output: 19
Explaination: 8, 9, 10, 11, 12, 13, 14, 15, 
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
26 have 2 as integral part of there cube root.
Your Task:
You do not need to read input or print anything. Your task is to complete the function integralRoot() which takes N and K as input parameters and returns the number of possible integers which have N as Kth root of the integer.
Expected Time Complexity: O(LogK)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 100
1 ≤ K ≤ 8
"""

def integral_root_count(N: int, K: int) -> int:
    """
    Calculate the number of integers n such that N is the integral part of the Kth root of n.

    Parameters:
    - N (int): The integral part of the Kth root.
    - K (int): The root to be considered (e.g., 2 for square root, 3 for cube root).

    Returns:
    - int: The number of possible integers n.
    """
    return pow(N + 1, K) - pow(N, K)
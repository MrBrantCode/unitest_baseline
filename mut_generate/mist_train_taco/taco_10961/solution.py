"""
QUESTION:
Given a positive integer K. Find the number of ordered pairs of positive integers (a,b) where 1≤a<b<K such that a+b ≤ K.
 
Example 1:
Input:
K = 2
Output:
0
Explanation:
There are no solutions for K = 2.
Example 2:
Input:
K = 4
Output:
2
Explanation:
There are 2 solutions:- (1,2) and (1,3).
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numOfWays() which takes an Integer K as input and returns the number of solutions for a and b (1≤a<b<K) such that a+b ≤ K.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= K <= 10^{5}
"""

def count_ordered_pairs(K: int) -> int:
    """
    Counts the number of ordered pairs (a, b) where 1 ≤ a < b < K and a + b ≤ K.

    Parameters:
    K (int): The upper limit for the pairs (a, b).

    Returns:
    int: The number of valid ordered pairs (a, b).
    """
    return K // 2 * (K % 2 + K - 2) // 2
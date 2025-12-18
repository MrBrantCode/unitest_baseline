"""
QUESTION:
Given a set of n elements, find number of ways of partitioning it.
 
Example 1:
Input:
N = 2
Output: 2
Explanation:
Let the set be 
{1, 2}:
{ {1}, {2} } { {1, 2} }
 
Example 2:
Input:
N = 3
Output: 5
Your Task:  
You don't need to read input or print anything. Your task is to complete the function bellNumber() which takes the integer N as input parameters and returns the number of ways of partitioning n elements. Since the value can be quite large print the value modulo 10^{9}+7.
Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(N^2)
 
Constraints:
1 ≤ N ≤ 1000
"""

def bell_number(n: int) -> int:
    """
    Calculate the number of ways to partition a set of n elements.

    Parameters:
    n (int): The number of elements in the set.

    Returns:
    int: The number of ways to partition the set, modulo 10^9 + 7.
    """
    m = [[0] * (n + 1) for _ in range(n + 1)]
    m[0][0] = 1
    for i in range(1, n + 1):
        m[i][0] = m[i - 1][i - 1]
        for j in range(1, i + 1):
            m[i][j] = (m[i - 1][j - 1] + m[i][j - 1]) % 1000000007
    return m[n][0]
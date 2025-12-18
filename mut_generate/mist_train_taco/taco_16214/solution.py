"""
QUESTION:
Given a number N, the task is to find the number of diagonals in N sided convex polygon.
Example 1:
Input: N = 5
Output: 5
Example 2:
Input: N = 6
Output: 9
Your Task:  
You don't need to read input or print anything. Your task is to complete the function diagonals() which takes N as input and returns the number of possible diagonals.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
3 ≤ N ≤ 10^{9}
"""

def calculate_diagonals(n: int) -> int:
    """
    Calculate the number of diagonals in an n-sided convex polygon.

    Parameters:
    n (int): The number of sides in the convex polygon.

    Returns:
    int: The number of diagonals in the n-sided convex polygon.
    """
    return int(n * (n - 3) // 2)
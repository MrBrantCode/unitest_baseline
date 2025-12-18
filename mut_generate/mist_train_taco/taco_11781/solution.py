"""
QUESTION:
Given a positive integer N denoting the length of a stick, return the number of ways to split a stick into four parts so that it's possible to form a rectangle using these parts, but is impossible to form a square.
Example 1:
Input: N = 10
Output: 2
Explanation: The 2 ways to split 
the stick are {1,1,4,4} , {2,2,3,3} 
Ã¢â¬â¹Example 2:
Input: n = 20
Output: 4
Explanation: The 4 ways to split 
the stick are {1,1,9,9} , {2,2,8,8}, 
{3,3,7,7} and {4,4,6,6}. Note that 
{5,5,5,5} forms square so it is not 
considered.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function count() which takes N as input and returns the answer.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{9}
"""

def count_rectangular_splits(N: int) -> int:
    """
    Count the number of ways to split a stick of length N into four parts
    such that they can form a rectangle but not a square.

    Parameters:
    N (int): The length of the stick.

    Returns:
    int: The number of valid ways to split the stick.
    """
    if N % 2 != 0:
        return 0
    
    n = N // 2
    if n % 2 != 0:
        return n // 2
    
    return n // 2 - 1
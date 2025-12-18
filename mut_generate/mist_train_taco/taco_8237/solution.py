"""
QUESTION:
Given an integer n, find the nth Pentagonal number. First three pentagonal numbers are 1, 5 and 12 (Please see below diagram).The n’th pentagonal number P_{n} is the number of distinct dots in a pattern of dots consisting of the outlines of regular pentagons with sides up to n dots, when the pentagons are overlaid so that they share one vertex.
Pentagonal Number
Example 1:
Input:
n = 1 
Output:
1 
Explanation:
See the diagram given above.
Example 2:
Input:
n = 2 
Output:
5
Explanation:
See the diagram given above.
Example 3:
Input:
n = 3
Output:
12
Explanation:
See the diagram given above.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getNthPentagonalNum() which takes an Integer n as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= n <= 10^{5}
"""

def get_nth_pentagonal_number(n: int) -> int:
    """
    Calculate the nth pentagonal number.

    Parameters:
    n (int): The position of the pentagonal number to be calculated.

    Returns:
    int: The nth pentagonal number.
    """
    return int(3 * n * (n - 1) / 2 + n)
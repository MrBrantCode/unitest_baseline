"""
QUESTION:
A pair of two very large positive integers is given. Find their sum.
 
Example 1:
Input: s1 = "63457", s2 = "645"
Output: 64102
Explanation: 63457 + 645 = 64102
Example 2:
Input: s1 = "101", s2 = "102"
Output: 203
Explanation: 101 + 102 = 203
 
Your Task:
You don't need to read or print anything. Your task to complete the function add() which takes two numbers in string format as input parameter and returns their sum in string format.
 
Expected Time Complexity: O(max(len(s1), len(s2))
Expected Space Complexity: O(1)
 
Constraints:
1 <= |s1|, |s2| <= 100000
"""

def add_large_integers(s1: str, s2: str) -> str:
    """
    Adds two very large positive integers represented as strings.

    Parameters:
    - s1 (str): The first large positive integer as a string.
    - s2 (str): The second large positive integer as a string.

    Returns:
    - str: The sum of the two large integers as a string.
    """
    return str(int(s1) + int(s2))
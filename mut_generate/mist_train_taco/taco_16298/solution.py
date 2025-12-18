"""
QUESTION:
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek to build a star pattern.
 
Example 1:
Input: 5
Output:
* 
* * 
* * * 
* * * * 
* * * * *
 
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.
Constraints:
	1<= N <= 20
"""

def generate_star_triangle(n: int) -> list[str]:
    """
    Generates a star pattern triangle with 'n' rows.

    Parameters:
    n (int): The number of rows in the star pattern.

    Returns:
    list[str]: A list of strings where each string represents a row of the star pattern.
    """
    return ['* ' * i for i in range(1, n + 1)]
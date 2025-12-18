"""
QUESTION:
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek build a star pattern.
 
Example 1:
Input: 5
Output:
* * * * *
* * * * 
* * * 
* *  
* 
 
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.
Constraints:
	1<= N <= 20
"""

def generate_star_triangle(n: int) -> list[str]:
    triangle = []
    for i in range(n):
        row = '* ' * (n - i)
        triangle.append(row.strip())  # Strip trailing space for each row
    return triangle
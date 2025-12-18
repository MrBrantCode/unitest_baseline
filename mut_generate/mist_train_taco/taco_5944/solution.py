"""
QUESTION:
Geek is very fond of patterns. Once, his teacher gave him a square pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek to build a star pattern.
 
Example 1:
Input: 5
Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
 
Your Task:
You don't need to input anything. Complete the function printSquare() which takes  an integer n  as the input parameter and print the pattern.
Constraints:
	1<= N <= 20
"""

def generate_square_pattern(n: int) -> list[str]:
    pattern = []
    for i in range(n):
        row = '* ' * n
        pattern.append(row.strip())
    return pattern
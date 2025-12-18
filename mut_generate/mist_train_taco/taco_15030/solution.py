"""
QUESTION:
Geek is very fond of patterns. Once, his teacher gave him a square pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek to build the pattern.
 
Example 1:
Input: 4
Output:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
Your Task:
You don't need to input anything. Complete the function printSquare() which takes  an integer n  as the input parameter and print the pattern.
Constraints:
	1<= N <= 20
"""

def generate_square_pattern(n: int) -> list[str]:
    pattern = []
    for i in range(2 * n - 1):
        row = []
        for j in range(2 * n - 1):
            value = n - min(i, j, 2 * n - 2 - j, 2 * n - 2 - i)
            row.append(str(value))
        pattern.append(' '.join(row))
    return pattern
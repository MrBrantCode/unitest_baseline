"""
QUESTION:
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek to build a star pattern.
 
Example 1:
Input: 5
Output:
1 
0 1 
1 0 1
0 1 0 1 
1 0 1 0 1
 
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.
Constraints:
	1<= N <= 20
"""

def generate_star_pattern(n: int) -> list[str]:
    pattern = []
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        row = []
        for j in range(i + 1):
            row.append(str(start))
            start = 1 - start
        pattern.append(' '.join(row))
    return pattern
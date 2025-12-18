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
* * * *
* * *
* *
*
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.
Constraints:
	1<= N <= 20
"""

def generate_star_pattern(n: int) -> list[str]:
    pattern = []
    
    # Upper part of the pattern
    for i in range(1, n + 1):
        pattern.append('* ' * i)
    
    # Lower part of the pattern
    for j in range(n - 1, 0, -1):
        pattern.append('* ' * j)
    
    return pattern
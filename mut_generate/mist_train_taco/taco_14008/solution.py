"""
QUESTION:
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek to build the pattern.
 
Example 1:
Input: 5
Output:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes  an integer n  as the input parameter and print the pattern.
Constraints:
	1<= N <= 20
"""

def generate_pattern(n: int) -> list[str]:
    pattern = []
    
    # Upper part of the pattern
    for i in range(n):
        line = ''
        for j in range(n - i):
            line += '*'
        for j in range(2 * i):
            line += ' '
        for j in range(n - i):
            line += '*'
        pattern.append(line)
    
    # Lower part of the pattern
    for i in range(n):
        line = ''
        for j in range(i + 1):
            line += '*'
        for j in range(2 * (n - i - 1)):
            line += ' '
        for j in range(i + 1):
            line += '*'
        pattern.append(line)
    
    return pattern
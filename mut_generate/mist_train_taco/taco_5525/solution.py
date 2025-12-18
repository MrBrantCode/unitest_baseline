"""
QUESTION:
Geek is very fond of patterns. Once, his teacher gave him a pattern to solve. He gave Geek an integer n and asked him to build a pattern.
Help Geek to build the pattern.
Example 1:
Input: 4
Output:
   A
  ABA
 ABCBA
ABCDCBA
Your Task:
You don't need to input anything. Complete the function printTriangle() which takes an integer n  as the input parameter and prints the pattern.
Constraints:
	1<= N <= 20
"""

def generate_pattern(n: int) -> list[str]:
    pattern = []
    for i in range(n):
        row = ''
        num = 0
        
        # Add leading spaces
        for j in range(n - i - 1):
            row += ' '
        
        # Add ascending characters
        for j in range(i + 1):
            row += chr(65 + num)
            num += 1
        
        # Add descending characters
        p = num - 2
        for j in range(i):
            row += chr(65 + p)
            p -= 1
        
        pattern.append(row)
    
    return pattern
"""
QUESTION:
<image>

You can preview the image in better quality by the link: [http://assets.codeforces.com/files/656/without-text.png](//assets.codeforces.com/files/656/without-text.png)

Input

The only line of the input is a string (between 1 and 50 characters long, inclusive). Each character will be an alphanumeric character or a full stop ".".

Output

Output the required answer.

Examples

Input

Codeforces


Output

-87


Input

APRIL.1st


Output

17
"""

def calculate_string_value(s: str) -> int:
    alpha = 'abcdefghijklmnopqrstuvwxyz.0123456789'
    res = 0
    
    for c in s:
        x1 = int('@' < c and '[' > c)
        x2 = alpha.index(c.lower()) + 1
        x3 = int('`' < c and '{' > c)
        x4 = x1 * x2
        x5 = x2 * x3
        x6 = x4 - x5
        res += x6
    
    return res
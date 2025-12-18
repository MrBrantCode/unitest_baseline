"""
QUESTION:
Implement the recursive function given by the following rules and print the last 3 digits:

F(x, y) = {
  y + 1 when x = 0,
  F(x - 1, 1) when x > 0 and y = 0,
  F(x - 1, F(x, y - 1)) when x > 0 and y > 0
}  

Input Format
A single line containing two integers X,Y
1 ≤ X,Y ≤ 100000  

Output Format
The last three digits  

Input Constraints
X and Y are non-negative integers.
Problem Setter: Practo Tech Team

SAMPLE INPUT
1 100

SAMPLE OUTPUT
102

Explanation

Note: x and y are non-negative integers
"""

def compute_last_three_digits(x, y):
    if x == 0:
        return (y + 1) % 1000
    if x == 1:
        return (y + 2) % 1000
    if x == 2:
        return (2 * y + 3) % 1000
    if x == 3:
        r = 5
        add = 8
        for i in range(y):
            r = (add + r) % 1000
            add = (add * 2) % 1000
        return r
    if x == 4 and y == 0:
        return 13
    if (x == 4 and y == 1) or (x == 5 and y == 0):
        return 533

    return 733
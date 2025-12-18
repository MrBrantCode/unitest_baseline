"""
QUESTION:
Write a program which reads three integers a, b and c, and prints "Yes" if a < b < c, otherwise "No".

Constraints

* 0 ≤ a, b, c ≤ 100

Input

Three integers a, b and c separated by a single space are given in a line.

Output

Print "Yes" or "No" in a line.

Examples

Input

1 3 8


Output

Yes


Input

3 8 1


Output

No
"""

def is_ascending_order(a: int, b: int, c: int) -> str:
    if a < b and b < c:
        return 'Yes'
    else:
        return 'No'
"""
QUESTION:
Write a program which prints small/large/equal relation of given two integers a and b.

Constraints

* -1000 ≤ a, b ≤ 1000

Input

Two integers a and b separated by a single space are given in a line.

Output

For given two integers a and b, print


a < b


if a is less than b,


a > b


if a is greater than b, and


a == b


if a equals to b.

Examples

Input

1 2


Output

a


Input

4 3


Output

a > b


Input

5 5


Output

a == b
"""

def compare_integers(a: int, b: int) -> str:
    if a == b:
        return 'a == b'
    elif a < b:
        return 'a < b'
    else:
        return 'a > b'
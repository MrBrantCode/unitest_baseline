"""
QUESTION:
You are given two integers a and b. Determine if a+b=15 or a\times b=15 or neither holds.

Note that a+b=15 and a\times b=15 do not hold at the same time.

Constraints

* 1 \leq a,b \leq 15
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


a b


Output

If a+b=15, print `+`; if a\times b=15, print `*`; if neither holds, print `x`.

Examples

Input

4 11


Output

+


Input

3 5


Output

*


Input

1 1


Output

x
"""

def check_sum_product(a: int, b: int) -> str:
    if a * b == 15:
        return '*'
    elif a + b == 15:
        return '+'
    else:
        return 'x'
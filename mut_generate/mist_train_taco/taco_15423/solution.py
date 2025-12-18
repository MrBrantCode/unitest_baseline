"""
QUESTION:
Does \sqrt{a} + \sqrt{b} < \sqrt{c} hold?

Constraints

* 1 \leq a, b, c \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


a \ b \ c


Output

If \sqrt{a} + \sqrt{b} < \sqrt{c}, print `Yes`; otherwise, print `No`.

Examples

Input

2 3 9


Output

No


Input

2 3 10


Output

Yes
"""

def is_sqrt_sum_less(a: int, b: int, c: int) -> str:
    if 4 * a * b < (c - a - b) ** 2 and c > a + b:
        return 'Yes'
    else:
        return 'No'
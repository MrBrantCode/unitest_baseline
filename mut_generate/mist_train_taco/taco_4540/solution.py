"""
QUESTION:
Find the least common multiple (LCM) of given n integers.

Constraints

* 2 ≤ n ≤ 10
* 1 ≤ ai ≤ 1000
* Product of given integers ai(i = 1, 2, ... n) does not exceed 231-1

Input


n
a1 a2 ... an


n is given in the first line. Then, n integers are given in the second line.

Output

Print the least common multiple of the given integers in a line.

Examples

Input

3
3 4 6


Output

12


Input

4
1 2 3 5


Output

30
"""

from functools import reduce
import math

def calculate_lcm(numbers):
    def lcm_base(x, y):
        return x * y // math.gcd(x, y)
    
    return reduce(lcm_base, numbers, 1)
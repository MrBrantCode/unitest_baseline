"""
QUESTION:
There are N integers a_1, a_2, ..., a_N not less than 1. The values of a_1, a_2, ..., a_N are not known, but it is known that a_1 \times a_2 \times ... \times a_N = P.

Find the maximum possible greatest common divisor of a_1, a_2, ..., a_N.

Constraints

* 1 \leq N \leq 10^{12}
* 1 \leq P \leq 10^{12}

Input

Input is given from Standard Input in the following format:


N P


Output

Print the answer.

Examples

Input

3 24


Output

2


Input

5 1


Output

1


Input

1 111


Output

111


Input

4 972439611840


Output

206
"""

import math
import collections

def max_gcd_from_product(N, P):
    def trial_division(n):
        factor = []
        tmp = int(math.sqrt(n)) + 1
        for num in range(2, tmp):
            while n % num == 0:
                n //= num
                factor.append(num)
        if not factor:
            return [n]
        else:
            factor.append(n)
            return factor
    
    lst = trial_division(P)
    c_lst = collections.Counter(lst)
    ans = 1
    for (k, v) in c_lst.items():
        while v >= N:
            ans *= k
            v -= N
    return ans
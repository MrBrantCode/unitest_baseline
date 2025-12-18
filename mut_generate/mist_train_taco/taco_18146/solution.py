"""
QUESTION:
Consider some positive integer $x$. Its prime factorization will be of form $x = 2^{k_1} \cdot 3^{k_2} \cdot 5^{k_3} \cdot \dots$

Let's call $x$ elegant if the greatest common divisor of the sequence $k_1, k_2, \dots$ is equal to $1$. For example, numbers $5 = 5^1$, $12 = 2^2 \cdot 3$, $72 = 2^3 \cdot 3^2$ are elegant and numbers $8 = 2^3$ ($GCD = 3$), $2500 = 2^2 \cdot 5^4$ ($GCD = 2$) are not.

Count the number of elegant integers from $2$ to $n$.

Each testcase contains several values of $n$, for each of them you are required to solve the problem separately.


-----Input-----

The first line contains a single integer $T$ ($1 \le T \le 10^5$) — the number of values of $n$ in the testcase.

Each of the next $T$ lines contains a single integer $n_i$ ($2 \le n_i \le 10^{18}$).


-----Output-----

Print $T$ lines — the $i$-th line should contain the number of elegant numbers from $2$ to $n_i$.


-----Example-----
Input
4
4
2
72
10

Output
2
1
61
6



-----Note-----

Here is the list of non-elegant numbers up to $10$:

  $4 = 2^2, GCD = 2$;  $8 = 2^3, GCD = 3$;  $9 = 3^2, GCD = 2$. 

The rest have $GCD = 1$.
"""

from math import sqrt, log2
from bisect import bisect

def all_primes(n):
    res = []
    for i in range(1, n + 1):
        prime = True
        for j in range(2, min(int(sqrt(i)) + 2, i)):
            if i % j == 0:
                prime = False
                break
        if prime:
            res.append(i)
    return res

def count_pow_nums(n, p):
    top = int(pow(n, 1.0 / p))
    if pow(top + 2, p) <= n:
        return top + 1
    elif pow(top + 1, p) <= n:
        return top
    elif pow(top, p) <= n:
        return top - 1
    else:
        return top - 2

def count_elegant_numbers(n):
    primes = all_primes(64)
    num_set = set()
    max_n = 1000000000000000000
    
    for pi in range(3, len(primes)):
        p = primes[pi]
        cnt = count_pow_nums(max_n, p)
        for num in range(2, cnt + 5):
            sq2 = round(sqrt(num))
            sq3 = round(pow(num, 1 / 3))
            if sq2 ** 2 != num and sq3 ** 3 != num:
                power_num = pow(num, p)
                if power_num <= max_n:
                    num_set.add(power_num)
    
    nums = sorted(num_set)
    
    ans = n - 1 - count_pow_nums(n, 2) - count_pow_nums(n, 3) + count_pow_nums(n, 6)
    ans -= bisect(nums, n)
    
    return ans
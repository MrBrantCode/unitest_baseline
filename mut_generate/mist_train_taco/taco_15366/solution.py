"""
QUESTION:
We call a positive integer number fair if it is divisible by each of its nonzero digits. For example, $102$ is fair (because it is divisible by $1$ and $2$), but $282$ is not, because it isn't divisible by $8$. Given a positive integer $n$. Find the minimum integer $x$, such that $n \leq x$ and $x$ is fair.


-----Input-----

The first line contains number of test cases $t$ ($1 \leq t \leq 10^3$). Each of the next $t$ lines contains an integer $n$ ($1 \leq n \leq 10^{18}$).


-----Output-----

For each of $t$ test cases print a single integer — the least fair number, which is not less than $n$.


-----Examples-----

Input
4
1
282
1234567890
1000000000000000000
Output
1
288
1234568040
1000000000000000000


-----Note-----

Explanations for some test cases:

In the first test case number $1$ is fair itself.

In the second test case number $288$ is fair (it's divisible by both $2$ and $8$). None of the numbers from $[282, 287]$ is fair, because, for example, none of them is divisible by $8$.
"""

import math

def lcm(lista):
    k = 1
    for i in lista:
        if i != 0:
            k = k * i // math.gcd(k, i)
    return k

def find_minimum_fair_number(n):
    a = str(n)
    listn = [int(i) for i in a]
    n_len = len(listn)
    
    for i in range(n_len):
        l = lcm(listn[:n_len - i - 1])
        nb = int(a[n_len - i - 1:])
        
        if i == n_len - 1:
            star = int(a)
        elif n % l == 0:
            star = nb
        else:
            temp = l - n % l
            star = temp + nb
        
        for m in range(star, 10 ** (i + 1), l):
            lsm = [int(i) for i in str(m)]
            lsm.append(l)
            lm = lcm(lsm)
            last = int(a[:n_len - i - 1] + '0' * (i + 1 - len(str(m))) + str(m))
            if last % lm == 0:
                return last
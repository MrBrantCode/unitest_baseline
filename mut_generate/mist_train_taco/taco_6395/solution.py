"""
QUESTION:
Let's call a positive integer composite if it has at least one divisor other than $1$ and itself. For example:

  the following numbers are composite: $1024$, $4$, $6$, $9$;  the following numbers are not composite: $13$, $1$, $2$, $3$, $37$. 

You are given a positive integer $n$. Find two composite integers $a,b$ such that $a-b=n$.

It can be proven that solution always exists.


-----Input-----

The input contains one integer $n$ ($1 \leq n \leq 10^7$): the given integer.


-----Output-----

Print two composite integers $a,b$ ($2 \leq a, b \leq 10^9, a-b=n$).

It can be proven, that solution always exists.

If there are several possible solutions, you can print any. 


-----Examples-----
Input
1

Output
9 8

Input
512

Output
4608 4096
"""

def delit(s):
    for i in range(2, s):
        if s % i == 0:
            return True
    return False

def find_composite_pair(n):
    if n % 2 == 0:
        a = n + 4
        b = 4
    else:
        a = n
        b = 3
        for i in range(10 ** 7):
            a += 1
            b = a - n
            if delit(b) and a % 4 == 0:
                break
    return (a, b)
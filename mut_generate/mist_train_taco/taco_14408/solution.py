"""
QUESTION:
Babu and Sabu are enemies but they fight with each other with the help of the mind games not guns. One day Babu asks Sabu to give the answer for this mathematical query as following:

Let f(m, n) = m^n

But Sabu is little weak in mathematics and he wants the help to answer the question.

Your aim is to answer f(m1, n1)^f(m2,n2) % n

Can you help Sabu to give answer of question to Babu.

INPUT:

You are given T which is the number of queries to solve.

Each Query consist of 5 space separated integers m1, n1, m2, n2, n.

OUTPUT:

Output contains exactly T lines. i th line containing the answer for the i th query.

Constraints:

1 ≤ T ≤ 10000 

0 ≤ m1, n1, m2, n2, n ≤ 1000000000

1 ≤ n ≤ 10000000

SAMPLE INPUT
1
2 1 2 2 15

SAMPLE OUTPUT
1
"""

def calculate_query_result(m1, n1, m2, n2, n):
    def totient(n):
        result = 1
        p = 2
        while p**2 <= n:
            if n % p == 0:
                result *= (p - 1)
                n //= p
            while n % p == 0:
                result *= p
                n //= p
            if p == 2:
                p += 1
            else:
                p += 2
        if n != 1:
            result *= (n - 1)
        return result

    def modpow(p, z, b, c, m):
        if m == 2:
            return p % m
        cp = 0
        while m % p == 0:
            cp += 1
            m //= p
        t = totient(m)
        exponent = ((pow(b, c, t) * z) % t + t - (cp % t)) % t
        return pow(p, cp) * pow(p, exponent, m)

    def solve(a, b, c, m):
        result = 1
        p = 2
        while p**2 <= a:
            cp = 0
            while a % p == 0:
                a //= p
                cp += 1
            if cp != 0:
                temp = modpow(p, cp, b, c, m)
                result *= temp
                result %= m
            p += 1
        if a != 1:
            result *= modpow(a, 1, b, c, m)
        return result % m

    x = pow(m1, n1, n)
    if n == 1:
        return 0
    if x == 1:
        return 1
    if m2 < 10**2 and n2 < 10**1:
        y = pow(m2, n2)
        return pow(x, y, n)
    if x == 0:
        return 0
    return solve(x, m2, n2, n)
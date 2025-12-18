"""
QUESTION:
You are given two integers $a$ and $b$. Moreover, you are given a sequence $s_0, s_1, \dots, s_{n}$. All values in $s$ are integers $1$ or $-1$. It's known that sequence is $k$-periodic and $k$ divides $n+1$. In other words, for each $k \leq i \leq n$ it's satisfied that $s_{i} = s_{i - k}$.

Find out the non-negative remainder of division of $\sum \limits_{i=0}^{n} s_{i} a^{n - i} b^{i}$ by $10^{9} + 9$.

Note that the modulo is unusual!


-----Input-----

The first line contains four integers $n, a, b$ and $k$ $(1 \leq n \leq 10^{9}, 1 \leq a, b \leq 10^{9}, 1 \leq k \leq 10^{5})$.

The second line contains a sequence of length $k$ consisting of characters '+' and '-'. 

If the $i$-th character (0-indexed) is '+', then $s_{i} = 1$, otherwise $s_{i} = -1$.

Note that only the first $k$ members of the sequence are given, the rest can be obtained using the periodicity property.


-----Output-----

Output a single integer — value of given expression modulo $10^{9} + 9$.


-----Examples-----
Input
2 2 3 3
+-+

Output
7

Input
4 1 5 1
-

Output
999999228



-----Note-----

In the first example:

$(\sum \limits_{i=0}^{n} s_{i} a^{n - i} b^{i})$ = $2^{2} 3^{0} - 2^{1} 3^{1} + 2^{0} 3^{2}$ = 7

In the second example:

$(\sum \limits_{i=0}^{n} s_{i} a^{n - i} b^{i}) = -1^{4} 5^{0} - 1^{3} 5^{1} - 1^{2} 5^{2} - 1^{1} 5^{3} - 1^{0} 5^{4} = -781 \equiv 999999228 \pmod{10^{9} + 9}$.
"""

def calculate_remainder(n, a, b, k, sequence):
    p = 10**9 + 9
    
    # Convert sequence to list of integers (1 or -1)
    S = [1 if char == '+' else -1 for char in sequence]
    
    def pow_mod(x, y, p):
        number = 1
        while y:
            if y & 1:
                number = number * x % p
            y >>= 1
            x = x * x % p
        return number % p
    
    def inv(x, p):
        if 1 < x:
            return p - inv(p % x, x) * p // x
        return 1
    
    def v(p, a, b, k):
        i = 1
        while pow_mod(a, k, (10 ** 9 + 9) ** i) - pow_mod(b, k, (10 ** 9 + 9) ** i) == 0:
            i += 1
        return i - 1
    
    s = 0
    if a != b:
        vp = p ** v(p, a, b, k)
        sum_mod = (pow_mod(a, n + 1, p * vp) - pow_mod(b, n + 1, p * vp)) // vp * inv((pow_mod(a, k, p * vp) - pow_mod(b, k, p * vp)) // vp % p, p)
        pa = pow_mod(a, k - 1, p)
        pb = 1
        inv_a = inv(a, p)
        for i in range(k):
            s += S[i] * pa * pb * sum_mod % p
            pa = pa * inv_a % p
            pb = pb * b % p
    else:
        for i in range(k):
            s += S[i] * (n + 1) // k
        s *= pow_mod(a, n, p)
    
    s %= p
    return s
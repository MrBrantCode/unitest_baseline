"""
QUESTION:
The campus has $m$ rooms numbered from $0$ to $m - 1$. Also the $x$-mouse lives in the campus. The $x$-mouse is not just a mouse: each second $x$-mouse moves from room $i$ to the room $i \cdot x \mod{m}$ (in fact, it teleports from one room to another since it doesn't visit any intermediate room). Starting position of the $x$-mouse is unknown.

You are responsible to catch the $x$-mouse in the campus, so you are guessing about minimum possible number of traps (one trap in one room) you need to place. You are sure that if the $x$-mouse enters a trapped room, it immediately gets caught.

And the only observation you made is $\text{GCD} (x, m) = 1$.


-----Input-----

The only line contains two integers $m$ and $x$ ($2 \le m \le 10^{14}$, $1 \le x < m$, $\text{GCD} (x, m) = 1$) — the number of rooms and the parameter of $x$-mouse. 


-----Output-----

Print the only integer — minimum number of traps you need to install to catch the $x$-mouse.


-----Examples-----
Input
4 3

Output
3

Input
5 2

Output
2



-----Note-----

In the first example you can, for example, put traps in rooms $0$, $2$, $3$. If the $x$-mouse starts in one of this rooms it will be caught immediately. If $x$-mouse starts in the $1$-st rooms then it will move to the room $3$, where it will be caught.

In the second example you can put one trap in room $0$ and one trap in any other room since $x$-mouse will visit all rooms $1..m-1$ if it will start in any of these rooms.
"""

from math import gcd

def powmod(a, b, m):
    a %= m
    r = 1
    while b:
        if b & 1:
            r = r * a % m
        a = a * a % m
        b >>= 1
    return r

def prime_factors(n):
    if n & 1 == 0:
        e = 0
        while n & 1 == 0:
            n >>= 1
            e += 1
        yield (2, e)
    p = 3
    while n > 1:
        if p * p > n:
            p = n
        if n % p:
            p += 2
            continue
        e = 1
        n //= p
        while n % p == 0:
            n //= p
            e += 1
        yield (p, e)
        p += 2

def minimum_traps_needed(m, x):
    r = [(1, 1)]
    for (p, e) in prime_factors(m):
        assert e >= 1
        ord = p - 1
        assert powmod(x, ord, p) == 1
        for (pi, ei) in prime_factors(p - 1):
            while ord % pi == 0 and powmod(x, ord // pi, p) == 1:
                ord //= pi
        ords = [(1, 1), (ord, p - 1)]
        q = p
        for v in range(2, e + 1):
            q *= p
            if powmod(x, ord, q) != 1:
                ord *= p
            assert powmod(x, ord, q) == 1
            ords.append((ord, q // p * (p - 1)))
        r = [(a // gcd(a, c) * c, b * d) for (a, b) in r for (c, d) in ords]
    return sum((y // x for (x, y) in r))
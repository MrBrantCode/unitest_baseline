"""
QUESTION:
Let's call the set of positive integers $S$ correct if the following two conditions are met:

$S \subseteq \{1, 2, \dots, n\}$;

if $a \in S$ and $b \in S$, then $|a-b| \neq x$ and $|a-b| \neq y$.

For the given values $n$, $x$, and $y$, you have to find the maximum size of the correct set.


-----Input-----

A single line contains three integers $n$, $x$ and $y$ ($1 \le n \le 10^9$; $1 \le x, y \le 22$).


-----Output-----

Print one integer — the maximum size of the correct set.


-----Examples-----

Input
10 2 5
Output
5
Input
21 4 6
Output
9
Input
1337 7 7
Output
672
Input
455678451 22 17
Output
221997195


-----Note-----

None
"""

import math

def max_correct_set_size(n, x, y):
    def f(n, s):
        d = [-n, -n]
        d[s] = 0
        for i in range(y // g):
            d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
        return d[s]
    
    g = math.gcd(x, y)
    h = lambda n: max(f(n, 0), f(n, 1))
    y += x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)
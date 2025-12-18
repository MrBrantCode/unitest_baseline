"""
QUESTION:
Our hero - Maga has been working on a research related to Pascal’s Triangle for about a month. He has recently found a new problematic thing for his research. He has to calculate a big number. But he is very busy. Could you do it for him?

You are given a binomial as this: (a * x + b * y)^n. You have to find the binomial coefficient of x^k * y^(n-k) modulo 10^9+7.

Input:

You are given 4 integers: each space separated integers a, b, n and k.

Output:

Output 1 integer: the binomial coefficient of x^k * y^(n-k) mod (10^9+7).

Constraints:

1 ≤ a, b ≤ 100

1 ≤ n ≤ 10^6

1 ≤ k ≤ min(n,10^5)

SAMPLE INPUT
1 1 4 2

SAMPLE OUTPUT
6

Explanation

The result is 6. In the (x+y)^4 binomial, the coefficient of x^2 * y^2 is 6.
"""

def binomial_coefficient_modulo(a: int, b: int, n: int, k: int) -> int:
    mod = 1000000007

    def inv(x, y):
        res = 1
        while y:
            if y % 2:
                res = res * x % mod
            y //= 2
            x = x * x % mod
        return res

    num = 1
    deno = 1
    for i in range(1, n + 1):
        num = num * i % mod

    for i in range(1, k + 1):
        deno = deno * i % mod
        num = num * a % mod

    for i in range(1, n - k + 1):
        deno = deno * i % mod
        num = num * b % mod

    return num * inv(deno, mod - 2) % mod
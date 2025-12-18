"""
QUESTION:
You are given two integers a and b. Moreover, you are given a sequence s_0, s_1, ..., s_{n}. All values in s are integers 1 or -1. It's known that sequence is k-periodic and k divides n+1. In other words, for each k ≤ i ≤ n it's satisfied that s_{i} = s_{i - k}.

Find out the non-negative remainder of division of ∑ _{i=0}^{n} s_{i} a^{n - i} b^{i} by 10^{9} + 9.

Note that the modulo is unusual!

Input

The first line contains four integers n, a, b and k (1 ≤ n ≤ 10^{9}, 1 ≤ a, b ≤ 10^{9}, 1 ≤ k ≤ 10^{5}).

The second line contains a sequence of length k consisting of characters '+' and '-'. 

If the i-th character (0-indexed) is '+', then s_{i} = 1, otherwise s_{i} = -1.

Note that only the first k members of the sequence are given, the rest can be obtained using the periodicity property.

Output

Output a single integer — value of given expression modulo 10^{9} + 9.

Examples

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

Note

In the first example:

(∑ _{i=0}^{n} s_{i} a^{n - i} b^{i}) = 2^{2} 3^{0} - 2^{1} 3^{1} + 2^{0} 3^{2} = 7

In the second example:

(∑ _{i=0}^{n} s_{i} a^{n - i} b^{i}) = -1^{4} 5^{0} - 1^{3} 5^{1} - 1^{2} 5^{2} - 1^{1} 5^{3} - 1^{0} 5^{4} = -781 ≡ 999999228 \pmod{10^{9} + 9}.
"""

def calculate_remainder(n: int, a: int, b: int, k: int, s: str) -> int:
    mod = 1000000009
    ans = 0
    t = (n + 1) // k

    def modInverse(a):
        return pow(a, mod - 2, mod)

    i = 0
    for ind in range(len(s)):
        first = pow(a, n - i, mod) * pow(b, i, mod) % mod
        num = pow(b, k, mod) * modInverse(pow(a, k, mod)) % mod
        if b >= a:
            den = (num - 1 + mod) % mod
            num = (pow(num, t, mod) - 1 + mod) % mod
        else:
            den = (1 - num + mod) % mod
            num = (1 - pow(num, t, mod) + mod) % mod
        if num == 0:
            temp = t * first % mod
        else:
            temp = num * modInverse(den) % mod
            temp = temp * first % mod
        if s[ind] == '+':
            ans = (ans + temp) % mod
        elif s[ind] == '-':
            ans = (ans - temp + mod) % mod
        i += 1
        if i > n:
            i = 0
    return ans
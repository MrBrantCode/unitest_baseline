"""
QUESTION:
As a tradition, every year before IOI all the members of Natalia Fan Club are invited to Malek Dance Club to have a fun night together. Malek Dance Club has 2^{n} members and coincidentally Natalia Fan Club also has 2^{n} members. Each member of MDC is assigned a unique id i from 0 to 2^{n} - 1. The same holds for each member of NFC.

One of the parts of this tradition is one by one dance, where each member of MDC dances with a member of NFC. A dance pair is a pair of numbers (a, b) such that member a from MDC dances with member b from NFC.

The complexity of a pairs' assignment is the number of pairs of dancing pairs (a, b) and (c, d) such that a < c and b > d.

You are given a binary number of length n named x. We know that member i from MDC dances with member $i \oplus x$ from NFC. Your task is to calculate the complexity of this assignment modulo 1000000007 (10^9 + 7).

Expression $x \oplus y$ denotes applying «XOR» to numbers x and y. This operation exists in all modern programming languages, for example, in C++ and Java it denotes as «^», in Pascal — «xor».


-----Input-----

The first line of input contains a binary number x of lenght n, (1 ≤ n ≤ 100).

This number may contain leading zeros.


-----Output-----

Print the complexity of the given dance assignent modulo 1000000007 (10^9 + 7).


-----Examples-----
Input
11

Output
6

Input
01

Output
2

Input
1

Output
1
"""

def calculate_dance_complexity(x: str) -> int:
    div = 1000000007
    n = len(x)
    ans = 0
    mi = [1]
    
    # Precompute powers of 2 modulo div up to 100
    for i in range(100):
        mi.append(mi[-1] * 2 % div)
    
    # Calculate the complexity
    for i in range(n):
        if x[n - 1 - i] == '1':
            ret = mi[i] * mi[i] % div * mi[n - 1 - i] % div
            ans = (ans + ret) % div
    
    return ans
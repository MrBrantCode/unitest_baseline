"""
QUESTION:
You are given an integer array $a$ of length $n$.

Does there exist an array $b$ consisting of $n+1$ positive integers such that $a_i=\gcd (b_i,b_{i+1})$ for all $i$ ($1 \leq i \leq n$)?

Note that $\gcd(x, y)$ denotes the greatest common divisor (GCD) of integers $x$ and $y$.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \leq t \leq 10^5$). Description of the test cases follows.

The first line of each test case contains an integer $n$ ($1 \leq n \leq 10^5$) — the length of the array $a$.

The second line of each test case contains $n$ space-separated integers $a_1,a_2,\ldots,a_n$ representing the array $a$ ($1 \leq a_i \leq 10^4$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^5$.


-----Output-----

For each test case, output "YES" if such $b$ exists, otherwise output "NO". You can print each letter in any case (upper or lower).


-----Examples-----

Input
4
1
343
2
4 2
3
4 2 4
4
1 1 1 1
Output
YES
YES
NO
YES


-----Note-----

In the first test case, we can take $b=[343,343]$.

In the second test case, one possibility for $b$ is $b=[12,8,6]$.

In the third test case, it can be proved that there does not exist any array $b$ that fulfills all the conditions.
"""

import math

def can_form_array_b(test_cases):
    results = []
    for n, a in test_cases:
        if n == 1:
            results.append("YES")
        else:
            result = "YES"
            for x, y, z in zip(a, a[1:], a[2:]):
                if y % math.gcd(x, z) != 0:
                    result = "NO"
                    break
            results.append(result)
    return results
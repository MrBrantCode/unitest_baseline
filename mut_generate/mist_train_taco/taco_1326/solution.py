"""
QUESTION:
Penny has an array of $n$ integers, $[a_0,a_1,\ldots,a_{n-1}]$. She wants to find the number of unique multisets she can form using elements from the array such that the bitwise XOR of all the elements of the multiset is a prime number. Recall that a multiset is a set which can contain duplicate elements.

Given $\textit{q}$ queries where each query consists of an array of integers, can you help Penny find and print the number of valid multisets for each array? As these values can be quite large, modulo each answer by $10^9+7$ before printing it on a new line.

Input Format

The first line contains a single integer, $\textit{q}$, denoting the number of queries. The $2\cdot q$ subsequent lines describe each query in the following format:

The first line contains a single integer, $n$, denoting the number of integers in the array.
The second line contains $n$ space-separated integers describing the respective values of $a_0,a_1,\ldots,a_{n-1}$.

Constraints

$1\leq q\leq10$  
$1\leq n\leq1000000$
$3500\leq a_i\leq4500$

Output Format

On a new line for each query, print a single integer denoting the number of unique multisets Penny can construct using numbers from the array such that the bitwise XOR of all the multiset's elements is prime. As this value is quite large, your answer must be modulo $10^9+7$.

Sample Input
1   
3   
3511 3671 4153  

Sample Output
4

Explanation

The valid multisets are:

$\{3511\}\rightarrow3511$ is prime.
$\{3671\}\to3671$ is prime.
$\{4153\}\rightarrow4153$ is prime.
$\{3511,3671,4153\}\to3511\oplus3671\oplus4153\text{=5081}$, which is prime.

Because there are four valid multisets, we print the value of $4\%(10^9+7)=4$ on a new line.
"""

from collections import Counter
from math import sqrt

def primes(n):
    x = [True] * ((n - 1) // 2)
    for i in range(int((sqrt(n) - 3) // 2) + 1):
        if x[i]:
            x[2 * i * i + 6 * i + 3::2 * i + 3] = [False] * int((n - (2 * i + 3) ** 2) // (4 * i + 6) + 1)
    return [2] + [2 * i + 3 for (i, v) in enumerate(x) if v]

def count_prime_xor_multisets(numbers, modulo=10**9 + 7):
    counts = Counter(numbers).items()
    count = [0] * 4501
    for (i, n) in counts:
        count[i] = n
    path = ((4096, 4351), (4352, 4500), (3584, 4095), (3500, 3583))
    span = ((256, 0), (512, 0), (512, 4096), (1024, 4096))
    totals = [[0] * 8192 for _ in range(2)]
    (static, update) = (0, 1)
    totals[static][0] = 1
    for (i, p) in enumerate(path):
        for (j, n) in enumerate(count[p[0]:p[1] + 1]):
            if n:
                same = 1 + n // 2
                change = (n + 1) // 2
                o = span[i][1]
                for x in range(span[i][0]):
                    y = x ^ j + p[0]
                    totals[update][x] = totals[static][y] * change + totals[static][x] * same
                    totals[update][y] = totals[static][x] * change + totals[static][y] * same
                    if o:
                        totals[update][x + o] = totals[static][y + o] * change + totals[static][x + o] * same
                        totals[update][y + o] = totals[static][x + o] * change + totals[static][y + o] * same
                if totals[update][0] > 100000 * modulo:
                    for x in range(len(totals[update])):
                        totals[update][x] %= modulo
                (static, update) = (update, static)
    p = primes(8191)
    total = 0
    for prime in p:
        total += totals[static][prime]
    return total % modulo
"""
QUESTION:
You have an array a[1], a[2], ..., a[n], containing distinct integers from 1 to n. Your task is to sort this array in increasing order with the following operation (you may need to apply it multiple times):

  choose two indexes, i and j (1 ≤ i < j ≤ n; (j - i + 1) is a prime number);  swap the elements on positions i and j; in other words, you are allowed to apply the following sequence of assignments: tmp = a[i], a[i] = a[j], a[j] = tmp (tmp is a temporary variable). 

You do not need to minimize the number of used operations. However, you need to make sure that there are at most 5n operations.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^5). The next line contains n distinct integers a[1], a[2], ..., a[n] (1 ≤ a[i] ≤ n).


-----Output-----

In the first line, print integer k (0 ≤ k ≤ 5n) — the number of used operations. Next, print the operations. Each operation must be printed as "i j" (1 ≤ i < j ≤ n; (j - i + 1) is a prime).

If there are multiple answers, you can print any of them.


-----Examples-----
Input
3
3 2 1

Output
1
1 3

Input
2
1 2

Output
0

Input
4
4 2 3 1

Output
3
2 4
1 2
2 4
"""

import bisect

def gen_primes(upper_bound):
    upper_bound += 1
    t = [0] * upper_bound
    primes = [2]
    for i in range(3, upper_bound, 2):
        if t[i]:
            continue
        primes.append(i)
        for j in range(i + i, upper_bound, i):
            t[j] = 1
    return primes

def sort_array_with_prime_swaps(n, a):
    primes = gen_primes(n + 1)
    process = []
    d = [0] * n
    for i in range(n):
        d[a[i] - 1] = i
    i = 0
    while i < n:
        if a[i] == i + 1:
            i += 1
            continue
        r = d[i]
        l = r - primes[bisect.bisect(primes, r - i + 1) - 1] + 1
        (a[l], a[r]) = (a[r], a[l])
        process.append('{} {}'.format(l + 1, r + 1))
        d[a[l] - 1] = l
        d[a[r] - 1] = r
    k = len(process)
    return k, process
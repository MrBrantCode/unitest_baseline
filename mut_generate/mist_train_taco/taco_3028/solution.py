"""
QUESTION:
Iahub is so happy about inventing bubble sort graphs that he's staying all day long at the office and writing permutations. Iahubina is angry that she is no more important for Iahub. When Iahub goes away, Iahubina comes to his office and sabotage his research work.

The girl finds an important permutation for the research. The permutation contains n distinct integers a1, a2, ..., an (1 ≤ ai ≤ n). She replaces some of permutation elements with -1 value as a revenge. 

When Iahub finds out his important permutation is broken, he tries to recover it. The only thing he remembers about the permutation is it didn't have any fixed point. A fixed point for a permutation is an element ak which has value equal to k (ak = k). Your job is to proof to Iahub that trying to recover it is not a good idea. Output the number of permutations which could be originally Iahub's important permutation, modulo 1000000007 (109 + 7).

Input

The first line contains integer n (2 ≤ n ≤ 2000). On the second line, there are n integers, representing Iahub's important permutation after Iahubina replaces some values with -1. 

It's guaranteed that there are no fixed points in the given permutation. Also, the given sequence contains at least two numbers -1 and each positive number occurs in the sequence at most once. It's guaranteed that there is at least one suitable permutation.

Output

Output a single integer, the number of ways Iahub could recover his permutation, modulo 1000000007 (109 + 7).

Examples

Input

5
-1 -1 4 3 -1


Output

2

Note

For the first test example there are two permutations with no fixed points are [2, 5, 4, 3, 1] and [5, 1, 4, 3, 2]. Any other permutation would have at least one fixed point.
"""

def count_recoverable_permutations(n, permutation):
    mod = 10**9 + 7

    def even(n):
        return 1 if n % 2 == 0 else 0

    def pow(n, p, mod=mod):
        res = 1
        while p > 0:
            if p % 2 == 0:
                n = n ** 2 % mod
                p //= 2
            else:
                res = res * n % mod
                p -= 1
        return res % mod

    def factrial_memo(n=10**5, mod=mod):
        fact = [1, 1]
        for i in range(2, n + 1):
            fact.append(fact[-1] * i % mod)
        return fact

    fact = factrial_memo()

    def combination(n, r):
        return fact[n] * pow(fact[n - r], mod - 2) % mod * pow(fact[r], mod - 2) % mod

    ct = 0
    lst2 = [0] * 2001
    lst3 = [0] * 2001

    for i in range(n):
        if permutation[i] == -1:
            ct += 1
            lst3[i + 1] = 1
        else:
            lst2[permutation[i]] = 1

    ct2 = 0
    for i in range(1, n + 1):
        if lst3[i] == 1 and lst2[i] == 0:
            ct2 += 1

    ans = 0
    for i in range(ct2 + 1):
        ans += pow(-1, i) * combination(ct2, i) * fact[ct - i]
        ans %= mod

    return ans
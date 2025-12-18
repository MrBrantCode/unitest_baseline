"""
QUESTION:
Takahashi and Aoki are going to together construct a sequence of integers.
First, Takahashi will provide a sequence of integers a, satisfying all of the following conditions:
 - The length of a is N.
 - Each element in a is an integer between 1 and K, inclusive.
 - a is a palindrome, that is, reversing the order of elements in a will result in the same sequence as the original.
Then, Aoki will perform the following operation an arbitrary number of times:
 - Move the first element in a to the end of a.
How many sequences a can be obtained after this procedure, modulo 10^9+7?

-----Constraints-----
 - 1≤N≤10^9
 - 1≤K≤10^9

-----Input-----
The input is given from Standard Input in the following format:
N K

-----Output-----
Print the number of the sequences a that can be obtained after the procedure, modulo 10^9+7.

-----Sample Input-----
4 2

-----Sample Output-----
6

The following six sequences can be obtained:
 - (1, 1, 1, 1)
 - (1, 1, 2, 2)
 - (1, 2, 2, 1)
 - (2, 2, 1, 1)
 - (2, 1, 1, 2)
 - (2, 2, 2, 2)
"""

from math import gcd

def divisors(M):
    d = []
    i = 1
    while M >= i ** 2:
        if M % i == 0:
            d.append(i)
            if i ** 2 != M:
                d.append(M // i)
        i += 1
    d.sort()
    return d

def count_palindrome_sequences(N, K):
    mod = 10 ** 9 + 7
    div = divisors(N)
    res = [0 for _ in range(len(div))]
    ans = 0
    
    if N % 2 == 0:
        for i in range(len(div)):
            d = div[i]
            g = gcd(2 * d, N)
            res[i] += pow(K, g // 2, mod)
            res[i] %= mod
            ans += d * res[i]
            ans %= mod
            for j in range(i + 1, len(div)):
                if div[j] % d == 0:
                    res[j] -= res[i]
                    res[j] %= mod
    else:
        for i in range(len(div)):
            d = div[i]
            g = gcd(2 * d, N)
            res[i] += pow(K, (g + 1) // 2, mod)
            res[i] %= mod
            ans += d * res[i]
            ans %= mod
            for j in range(i + 1, len(div)):
                if div[j] % d == 0:
                    res[j] -= res[i]
                    res[j] %= mod
    
    return ans % mod
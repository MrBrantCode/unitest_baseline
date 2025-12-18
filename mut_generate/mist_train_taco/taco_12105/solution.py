"""
QUESTION:
problem

Given two strings, find the longest of the strings contained in both strings and write a program that answers that length.

Here, the string s included in the string t means that s appears consecutively in t. An empty string, that is, a string of length 0, is included in any string. For example, the string ABRACADABRA contains the following strings: ABRA, RAC, D, ACADABRA, ABRACADABRA, the empty string, etc. On the other hand, the string ABRACADABRA does not contain the following strings: ABRC, RAA, BA , K etc.



input

The input consists of multiple datasets. Each dataset is given in the following format.

The input consists of two lines, the first line is given the first string and the second line is given the second string. The strings consist of uppercase letters and each string is 1 in length. More than 4000 and less.

Of the scoring data, for 30% of the points, the length of each character string is 1 or more and 50 or less.

The end of input is indicated by EOF. The number of datasets does not exceed 10.

output

Outputs the length of the longest string contained in both of the two strings given for each dataset on one line.

Examples

Input

ABRACADABRA
ECADADABRBCRDARA
UPWJCIRUCAXIIRGL
SBQNYBSBZDFNEV


Output

5
0


Input

None


Output

None
"""

def longest_common_substring_length(S, T):
    MOD = 358976445361682909
    base = 31

    def rolling_hash(string, base, MOD):
        l = len(string)
        h = [0] * (l + 1)
        for i in range(l):
            h[i + 1] = (h[i] * base + ord(string[i])) % MOD
        return h

    rhs = rolling_hash(S, base, MOD)
    rht = rolling_hash(T, base, MOD)
    L = len(S)
    M = len(T)

    def solve(l):
        v = pow(base, l, MOD)
        hs = set()
        for i in range(L - l + 1):
            hs.add((rhs[i + l] - rhs[i] * v) % MOD)
        for i in range(M - l + 1):
            if (rht[i + l] - rht[i] * v) % MOD in hs:
                return 1
        return 0

    left = 0
    right = min(L, M) + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if solve(mid):
            left = mid
        else:
            right = mid

    return left
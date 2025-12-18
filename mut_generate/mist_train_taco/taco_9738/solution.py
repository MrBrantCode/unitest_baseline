"""
QUESTION:
Watto, the owner of a spare parts store, has recently got an order for the mechanism that can process strings in a certain way. Initially the memory of the mechanism is filled with n strings. Then the mechanism should be able to process queries of the following type: "Given string s, determine if the memory of the mechanism contains string t that consists of the same number of characters as s and differs from s in exactly one position".

Watto has already compiled the mechanism, all that's left is to write a program for it and check it on the data consisting of n initial lines and m queries. He decided to entrust this job to you.


-----Input-----

The first line contains two non-negative numbers n and m (0 ≤ n ≤ 3·10^5, 0 ≤ m ≤ 3·10^5) — the number of the initial strings and the number of queries, respectively.

Next follow n non-empty strings that are uploaded to the memory of the mechanism.

Next follow m non-empty strings that are the queries to the mechanism.

The total length of lines in the input doesn't exceed 6·10^5. Each line consists only of letters 'a', 'b', 'c'.


-----Output-----

For each query print on a single line "YES" (without the quotes), if the memory of the mechanism contains the required string, otherwise print "NO" (without the quotes).


-----Examples-----
Input
2 3
aaaaa
acacaca
aabaa
ccacacc
caaac

Output
YES
NO
NO
"""

def check_similar_strings(initial_strings, queries):
    mod = 9999999999999983
    v = set()
    
    # Process initial strings
    for s in initial_strings:
        l = len(s)
        pow = 1
        h = 0
        for i in range(l):
            h = (h + ord(s[i]) * pow) % mod
            pow = pow * 203 % mod
        pow = 1
        for i in range(l):
            for j in range(97, 100):
                if ord(s[i]) != j:
                    v.add((h + (j - ord(s[i])) * pow) % mod)
            pow = pow * 203 % mod
    
    # Process queries
    results = []
    for s in queries:
        pow = 1
        h = 0
        for i in range(len(s)):
            h = (h + ord(s[i]) * pow) % mod
            pow = pow * 203 % mod
        results.append('YES' if h in v else 'NO')
    
    return results
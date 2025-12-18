"""
QUESTION:
You are given a string S and Q query strings (q1, q2, ... , qQ). For each query string, report whether or not it is a subsequence of S.

Input :

The first line contains a string S.

The next line contains a single integer, Q.

The following Q lines each contain 1 query string qi.

Output :

Output Q lines. On the i^th line print "Yes" (without quotes) if qi is a sub-sequence of S, otherwise print "No"  (without quotes).

Constraints :

1 ≤ |S|, |q[i]|, Q ≤ 100,000

Sum of lengths of all query strings ≤ 1,000,000 

All strings consist of lowercase english letters only. ('a'-'z')

SAMPLE INPUT
hello
5
world
lo
elo
hl
ol

SAMPLE OUTPUT
No
Yes
Yes
Yes
No
"""

def is_subsequence_for_queries(S, queries):
    n = len(S)
    nxt = [[n for _ in range(26)] for _ in range(n + 1)]
    
    # Preprocess the string S to build the nxt array
    for i in reversed(range(n)):
        nxt[i] = nxt[i + 1][:]
        nxt[i][ord(S[i]) - 97] = i
    
    results = []
    
    # Process each query string
    for query in queries:
        i, isGood = 0, True
        for c in query:
            if i < n and nxt[i][ord(c) - 97] < n:
                i = nxt[i][ord(c) - 97] + 1
            else:
                isGood = False
                break
        results.append('Yes' if isGood else 'No')
    
    return results
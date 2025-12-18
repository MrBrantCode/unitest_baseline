"""
QUESTION:
Solve the mystery.
Input:
First line contains a single integer denoting number of test cases(T).
Next T lines have one test case per line.
Each test case is a string of alphabets [a-z].

Output:
Print answer to each test case in an individual line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |S| ≤ 100
a ≤ S[i] ≤ z

Problem Setter : Siddharth Seth

SAMPLE INPUT
5
malayalam
ariyama
alla
brook
kurruk

SAMPLE OUTPUT
121
-1
108
-1
114
"""

def solve_mystery(test_cases):
    results = []
    for s in test_cases:
        rev = s[::-1]
        if s == rev:
            ch = s[len(s) // 2]
            results.append(ord(ch))
        else:
            results.append(-1)
    return results
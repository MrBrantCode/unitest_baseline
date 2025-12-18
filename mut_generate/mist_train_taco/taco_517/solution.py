"""
QUESTION:
Yash has recently learnt about the Fibonacci sequence and is very excited about it. He calls a sequence Fibonacci-ish if   the sequence consists of at least two elements  f_0 and f_1 are arbitrary  f_{n} + 2 = f_{n} + 1 + f_{n} for all n ≥ 0. 

You are given some sequence of integers a_1, a_2, ..., a_{n}. Your task is rearrange elements of this sequence in such a way that its longest possible prefix is Fibonacci-ish sequence.


-----Input-----

The first line of the input contains a single integer n (2 ≤ n ≤ 1000) — the length of the sequence a_{i}.

The second line contains n integers a_1, a_2, ..., a_{n} (|a_{i}| ≤ 10^9).


-----Output-----

Print the length of the longest possible Fibonacci-ish prefix of the given sequence after rearrangement.


-----Examples-----
Input
3
1 2 -1

Output
3

Input
5
28 35 7 14 21

Output
4



-----Note-----

In the first sample, if we rearrange elements of the sequence as  - 1, 2, 1, the whole sequence a_{i} would be Fibonacci-ish.

In the second sample, the optimal way to rearrange elements is $7$, $14$, $21$, $35$, 28.
"""

from collections import Counter

def longest_fibonacci_ish_prefix(n, sequence):
    s = Counter(sequence)
    max_length = 0
    
    for q in s:
        s[q] -= 1
        for a in s:
            if not s[a]:
                continue
            t = [a]
            s[a] -= 1
            b = q + a
            while s.get(b, 0):
                s[b] -= 1
                t.append(b)
                (a, b) = (b, a + b)
            max_length = max(max_length, len(t))
            for c in t:
                s[c] += 1
        s[q] += 1
    
    return max_length + 1
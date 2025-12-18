"""
QUESTION:
problem

Given the sequence $ A $ of length $ N $. Find the maximum value of $ \ sum B_i $, where $ B $ is one of the longest increasing subsequences of the sequence $ A $.

The longest increasing subsequence of the sequence $ A $ is the longest subsequence that satisfies $ A_i <A_j $ with all $ i <j $.



output

Output the maximum value of $ \ sum B_i $, where $ B $ is one of the longest increasing subsequences of the sequence $ A $. Also, output a line break at the end.

Example

Input

4
6 4 7 8


Output

21
"""

import bisect

def max_sum_of_longest_increasing_subsequence(A):
    lis = []
    hist = []
    
    for a in A:
        i = bisect.bisect_left(lis, a)
        if i == len(lis):
            lis.append(a)
            hist.append([a])
        else:
            lis[i] = a
            hist[i].append(a)
    
    ans = last = hist[-1][0]
    for row in reversed(hist[:-1]):
        i = bisect.bisect_left(row[::-1], last)
        last = row[-i]
        ans += last
    
    return ans
"""
QUESTION:
Write a function `count_pairs` that takes a list of numbers `lst` and a target sum `tsum` as input, and returns the number of unique pairs in the list whose sum equals `tsum`. The function should not count duplicate pairs, i.e., if a pair (a, b) is counted, then (b, a) should not be counted separately. The function should not use any built-in Python functions or libraries.
"""

def count_pairs(lst, tsum):
    n = len(lst)
    cnt = 0
    checked_pairs = []
    for i in range(0, n):
        for j in range(i+1, n):
            if lst[i] + lst[j] == tsum:
                if [lst[i], lst[j]] not in checked_pairs and [lst[j], lst[i]] not in checked_pairs:
                    cnt += 1
                    checked_pairs.append([lst[i], lst[j]])
    return cnt
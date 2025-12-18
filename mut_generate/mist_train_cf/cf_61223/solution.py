"""
QUESTION:
Given a list of integers, write a function `longest_increasing_subsequence` that returns the longest increasing subsequence consisting of consecutive elements without considering their indices. The subsequence should be in the same order as it appears in the original list. If the input list is empty, the function should return an empty list.
"""

def longest_increasing_subsequence(lst):
    if not lst: 
        return []

    subsequences = [[lst[0]]]
    for i in range(1, len(lst)):
        if lst[i] > subsequences[-1][-1]:
            subsequences[-1].append(lst[i])
        else:
            subsequences.append([lst[i]])
            
    return max(subsequences, key=len)
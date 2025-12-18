"""
QUESTION:
Write a function `product_of_lcs_lengths(list1, list2)` that takes two lists of integers as input and returns the product of the lengths of all unique longest common substrings. The function should efficiently handle potentially large list inputs.
"""

from collections import defaultdict

def product_of_lcs_lengths(list1, list2):
    product = 1
    len1, len2 = len(list1), len(list2)
    lcs_lengths = defaultdict(int)
    max_len = 0

    dp = [[0]*(len2+1) for _ in range(len1+1)]
    
    for i in range(len1-1, -1, -1):
        for j in range(len2-1, -1, -1):
            if list1[i] == list2[j]:
                curr_len = dp[i+1][j+1] = dp[i+2][j+2] + 1 if i+2 < len1 and j+2 < len2 else 1
                if curr_len >= max_len:
                    if curr_len > max_len:
                        lcs_lengths.clear()
                        max_len = curr_len
                    lcs_lengths[tuple(list1[i:i+curr_len])] = curr_len
                     
    for length in lcs_lengths.values():
        product *= length
    return product
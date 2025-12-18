"""
QUESTION:
Implement a function `longest_inc_subsequence` that takes a list of integers as input and returns a tuple containing the length of the longest increasing subsequence consisting of consecutive elements, and the starting and ending indices of this subsequence in the original list. The function should only consider consecutive elements and their values, without considering their initial indices.
"""

def longest_inc_subsequence(lst):
    max_len = curr_len = 1
    max_start = curr_start = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            curr_len += 1
        else:
            if max_len < curr_len:
                max_len = curr_len
                max_start = curr_start
            curr_len = 1
            curr_start = i
    if max_len < curr_len:
        max_len = curr_len
        max_start = curr_start
    return max_len, max_start, max_start+max_len-1
"""
QUESTION:
Implement a function `longest_dec_subsequence(lst)` that takes a list of integers as input and returns a tuple containing the length of the longest decreasing subsequence consisting of consecutive elements, along with the starting and ending indices of this subsequence in the original list. The subsequence should be identified based on the values of the elements, regardless of their initial indices in the list. The function should handle lists of varying lengths and values.
"""

def longest_dec_subsequence(lst):
    max_len = curr_len = 1
    max_start = curr_start = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            curr_len += 1
        else:
            curr_len = 1
            curr_start = i
        if max_len < curr_len:
            max_len = curr_len
            max_start = curr_start
    max_end = max_start + max_len - 1
    return max_len, max_start, max_end
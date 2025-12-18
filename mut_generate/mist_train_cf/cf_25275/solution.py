"""
QUESTION:
Create a Python function `long_consec_sequence` that takes a list of integers as input and returns the length of the longest common subsequence of consecutive elements. The function should handle empty lists and lists with varying lengths.
"""

def longest_consecutive_subsequence(lst):
    if not lst:
        return 0

    max_seq_len = 0

    for i in range(len(lst)-1):
        curr_seq = 1
        j = i+1
        while (j < len(lst)):
            if (lst[j] - lst[j-1]) == 1:
                curr_seq += 1
            else:
                break
            j += 1

        if curr_seq > max_seq_len:
            max_seq_len = curr_seq

    return max_seq_len
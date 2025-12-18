"""
QUESTION:
Write a function `find_longest_seq` that takes a list of integers as input and returns the length of the longest consecutive sequence within the list. The sequence must be strictly increasing by 1.
"""

def find_longest_seq(arr):
    max_len = 0
    curr_seq = []
    for num in arr:
        if not curr_seq or num == curr_seq[-1] + 1:
            curr_seq.append(num)
            max_len = max(max_len, len(curr_seq))
        else: 
            curr_seq = [num]
    return max_len
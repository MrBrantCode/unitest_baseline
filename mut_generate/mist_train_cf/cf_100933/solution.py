"""
QUESTION:
Create a function called `max_contig_subarray` that takes an array of strings as input and returns the maximum contiguous sum of the lengths of a subarray such that no two strings in the subarray have any common characters. The function should utilize a hash table to keep track of the characters in each string. The time complexity of the algorithm should be optimized to reduce the number of string comparisons.
"""

def max_contig_subarray(arr):
    char_sets = [set(s) for s in arr]
    n = len(arr)
    max_len = 0
    cur_set = set()
    cur_len = 0
    i = 0
    j = 0
    while i < n and j < n:
        if len(cur_set.intersection(char_sets[j])) == 0:
            cur_set = cur_set.union(char_sets[j])
            cur_len += len(arr[j])
            j += 1
            max_len = max(max_len, cur_len)
        else:
            cur_set = cur_set.difference(char_sets[i])
            cur_len -= len(arr[i])
            i += 1
    return max_len
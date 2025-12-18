"""
QUESTION:
Write a function `partition_labels(S)` that takes a string `S` of lowercase English letters as input and returns a list of integers representing the size of the partitions of `S` such that each letter appears in at most one part and the sum of the ASCII values of the first character of each part is maximized. The string `S` will have a length in the range `[1, 500]` and will consist of only lowercase English letters.
"""

def partition_labels(S):
    last = {c: i for i, c in enumerate(S)}
    result = []
    anchor = j = 0
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            result.append(i - anchor + 1)
            anchor = i + 1
    return result
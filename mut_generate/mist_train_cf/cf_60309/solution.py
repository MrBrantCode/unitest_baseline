"""
QUESTION:
Create a function called `minDeletionSize` that takes a list of strings (`strs`) as input and returns the number of columns that need to be deleted to make the remaining columns sorted lexicographically. The input list contains `n` strings of equal length, where `1 <= n <= 100` and `1 <= strs[i].length <= 1000`. Each string `strs[i]` is composed of lowercase English letters.
"""

def minDeletionSize(strs):
    return sum(list(col) != sorted(col) for col in zip(*strs))
"""
QUESTION:
Write a function `longest_increasing_subsequence` that takes a list of integers `seqs` as input and returns the longest increasing subsequence (LIS) present in the sequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. An increasing subsequence is a subsequence in which the elements are in non-decreasing order. 

The input list `seqs` contains integers and may be empty. The function should return an empty list if `seqs` is empty. The function should return the longest increasing subsequence in the order it appears in the original sequence.
"""

from typing import List

def longest_increasing_subsequence(seqs: List[int]) -> List[int]:
    if not seqs:
        return []

    n = len(seqs)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if seqs[i] > seqs[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    max_index = lis.index(max_length)

    result = [seqs[max_index]]
    max_length -= 1

    for i in range(max_index - 1, -1, -1):
        if seqs[i] < seqs[max_index] and lis[i] == max_length:
            result.append(seqs[i])
            max_length -= 1
            max_index = i

    return result[::-1]
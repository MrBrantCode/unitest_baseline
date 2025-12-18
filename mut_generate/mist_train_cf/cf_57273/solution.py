"""
QUESTION:
Develop a Python function `find_kth_largest` that takes an unordered numerical sequence `num_list` and an integer `k` as input. The function should return the kth largest integer in the sequence, considering duplicate values as separate numbers. The function should be efficient and handle cases where k is within the bounds of the sequence.
"""

def find_kth_largest(num_list, k):
    num_list.sort(reverse=True)
    return num_list[k - 1]
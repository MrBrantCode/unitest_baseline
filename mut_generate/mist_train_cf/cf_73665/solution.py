"""
QUESTION:
Create a function named `cluster` that takes in a list of integers `nums` and an integer `size` as parameters. The function should return a list of clusters, where each cluster is a sublist of `nums` with a length of `size`, except for the last cluster, which may be smaller if the length of `nums` is not a multiple of `size`.
"""

def cluster(nums, size):
    return [nums[i:i+size] for i in range(0, len(nums), size)]
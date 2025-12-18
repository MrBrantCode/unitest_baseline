"""
QUESTION:
Write a function `find_combinations` that takes a list of integers `arr` and a target integer `target` as input, and returns all pairs of elements in `arr` that sum up to `target`. The function should use a hash map to optimize the solution.
"""

def find_combinations(arr, target):
    result = []
    buffer_map = dict()
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in buffer_map:
            result.append((complement, arr[i]))
        else:
            buffer_map[arr[i]] = i
    return result
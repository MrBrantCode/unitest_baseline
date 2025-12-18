"""
QUESTION:
Write a function called `count_subarrays` that takes a multi-dimensional array as input and returns a list of tuples, where each tuple contains a repeated sub-array and its frequency of occurrence. The function should handle sub-arrays with mixed data types and minimize state mutations, adhering to functional programming principles.
"""

def count_subarrays(arr):
    counts = {}
    for i in arr:
        key = ''.join(str(x) for x in i)
        counts[key] = counts.get(key, 0) + 1
    subarrays = [(tuple(map(lambda x: x if x != "' " else " ", k.replace('[', '').replace(']', '').replace("', '", ' ').split(','))), v) for k, v in counts.items() if v > 1]
    return subarrays
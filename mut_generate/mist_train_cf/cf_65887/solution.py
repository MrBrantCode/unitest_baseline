"""
QUESTION:
Write a function named `get_results` that takes an array of integers and a list of indices as inputs and returns a new array holding the cumulative sums of the original array elements corresponding to the given indices. The indices may be repeated, and the cumulative sum should reflect this.
"""

def get_results(arr, index):
    res = [0] * len(index)
    sums = [0] * len(arr)
    for i, idx in enumerate(index):
        sums[idx] += arr[idx]
        res[i] = sums[idx]
    return res
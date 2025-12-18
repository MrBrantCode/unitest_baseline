"""
QUESTION:
Write a function `partitionArray(arr, n)` that takes an array `arr` and an integer `n` as input, and returns a dictionary where the keys are the distinct elements from `arr` and the values are lists containing all instances of the corresponding key from `arr`, if the count of distinct elements in `arr` is greater than or equal to `n`. If the count of distinct elements is less than `n`, return an error message.
"""

def partitionArray(arr, n):
    arr_set = set(arr)
    if len(arr_set) < n:
        return 'The array does not have enough distinct elements.'

    else:
        sortedDict = {elem: [] for elem in arr_set}

        for elem in arr:
            sortedDict[elem].append(elem)

        return sortedDict
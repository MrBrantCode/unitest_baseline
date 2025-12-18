"""
QUESTION:
Write a function `find_most_common` that takes an array of integers as input and returns the most common value along with its frequency in a tuple. The array will contain at least 5 elements, have a maximum size of 100, and the elements will be integers between -1000 and 1000. In case of ties, return the value with the highest index in the array. The algorithm should have a time complexity of O(n).
"""

def find_most_common(arr):
    frequency = {}
    max_freq = 0
    max_value = None

    for i in range(len(arr)):
        if arr[i] in frequency:
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1

        if frequency[arr[i]] > max_freq or (frequency[arr[i]] == max_freq and i > arr.index(max_value) if max_value is not None else True):
            max_freq = frequency[arr[i]]
            max_value = arr[i]

    return (max_value, max_freq)
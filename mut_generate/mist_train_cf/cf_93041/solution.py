"""
QUESTION:
Write a function named `find_most_common` that takes an array of integers as input and returns a tuple containing the most common value and its frequency. The array will always contain at least 5 elements and at most 100 elements. The elements in the array are integers between -1000 and 1000. The function should have a time complexity of O(n). In case of ties, return the value with the highest index in the array.
"""

def find_most_common(arr):
    frequency = {}
    max_freq = 0
    max_value_index = -1

    for i in range(len(arr)):
        if arr[i] in frequency:
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1

        if frequency[arr[i]] > max_freq or (frequency[arr[i]] == max_freq and i > max_value_index):
            max_freq = frequency[arr[i]]
            max_value_index = i

    return (arr[max_value_index], max_freq)
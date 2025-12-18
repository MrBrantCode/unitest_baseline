"""
QUESTION:
Write a function `findLucky` that takes an array of integers as input. The function should return a lucky integer from the array, defined as an integer whose frequency within the array is equivalent to its actual value. If multiple lucky integers are present, return the one with the highest value. If the array does not contain any lucky integers, return -1. The array length is between 1 and 500, and each element is between 1 and 500.
"""

def findLucky(arr):
    freq_dict = {}
    max_lucky = -1

    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    for num, freq in freq_dict.items():
        if num == freq:
            max_lucky = max(max_lucky, num)

    return max_lucky
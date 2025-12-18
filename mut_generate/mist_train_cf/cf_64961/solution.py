"""
QUESTION:
Write a function called `find_unique` that takes an array of integers as input. The function should return the first number in the array that appears only once. If no such number exists, it should return None. The array may contain duplicate values.
"""

def find_unique(arr):
    freq = {}  # create an empty dictionary

    # populate the dictionary with the frequencies of each number
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # check for the first non-repeated number
    for num in arr:
        if freq[num] == 1:
            return num

    return None  # return None if all numbers are repeated
"""
QUESTION:
Write a function called `find_unique` that takes an array of integers as input and returns the index of the solitary unique value in the array. The array contains at least one unique integer and all other integers appear at least twice.
"""

def find_unique(arr):
    freq_count = {}  # Initialize an empty dictionary
    for i in range(len(arr)):
        if arr[i] not in freq_count:
            freq_count[arr[i]] = [i]  # the value will be a list containing the index
        else:
            freq_count[arr[i]].append(i)  # append the index to the list of indices

    # iterate through the dictionary values
    for value in freq_count.values():
        if len(value) == 1:  # check if the list containing indices has only one index
            return value[0]  # return the unique index
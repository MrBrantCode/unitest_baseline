"""
QUESTION:
Write a function `count_unique` that takes an array and its length as input, and returns the number of unique elements in the array without using any additional data structures such as arrays, hash maps, or sets.
"""

def count_unique(array):
    count = 0
    for i in range(len(array)):
        unique = 1
        for j in range(i):
            if array[i] == array[j]:
                unique = 0
                break
        count += unique
    return count
"""
QUESTION:
Find the function `find_missing_and_duplicates` that takes an array of integers as input and returns two values: a set of missing numbers from 1 to 1000 and a set of duplicate numbers in the array. The function should be efficient in terms of time and space complexity.
"""

import collections
def find_missing_and_duplicates(arr):
    all_numbers = set(range(1,1001))
    arr_set = set(arr)
    missing = all_numbers - arr_set
    counter = collections.Counter(arr)
    duplicates = set(item for item in counter if counter[item] > 1)
    return missing, duplicates
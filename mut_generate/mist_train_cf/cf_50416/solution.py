"""
QUESTION:
Design a function `find_divisible` that takes two integer arrays `arr1` and `arr2` as input. The function should return all the unique elements in `arr1` that are divisible by any element in `arr2`. The function should be optimized for time efficiency to handle large-scale data.
"""

def find_divisible(arr1, arr2):
    return [i for i in set(arr1) if any(i % j == 0 for j in arr2)]
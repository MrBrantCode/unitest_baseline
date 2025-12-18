"""
QUESTION:
Write a function `contains_duplicates` that checks if an array contains any duplicate elements. The function should return False if the array does not contain duplicates and True if it contains any. The input array can be unsorted and may contain duplicates. Implement the function with a time complexity less than or equal to O(nlogn) and a space complexity less than or equal to O(n).
"""

def contains_duplicates(arr):
    return len(arr) != len(set(arr))
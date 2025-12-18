"""
QUESTION:
Write a function `find_penultimate(arr)` to find the second smallest element in an array of distinct integers of length 'n'. The function should return the penultimate minimum value without modifying the original array.
"""

def find_penultimate(arr):
    return sorted(arr)[1]
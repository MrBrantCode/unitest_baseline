"""
QUESTION:
Write a function called `find_odd_element_index` that takes an array of integers as input and returns the index of the element that appears an odd number of times. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_odd_element_index(arr):
    result = 0
    for num in arr:
        result ^= num
    
    for i, num in enumerate(arr):
        if num == result:
            return i
"""
QUESTION:
Write a function named `count_element` that takes an array `arr` and an `element` as input and returns the number of occurrences of the `element` in the `arr`. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def count_element(arr, element):
    count = 0
    for i in arr:
        if i == element:
            count += 1
    return count
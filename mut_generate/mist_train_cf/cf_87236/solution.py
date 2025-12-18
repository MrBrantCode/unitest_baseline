"""
QUESTION:
Define a function `square_and_sort` that takes an array of integers, squares each value while treating negative numbers as positive, and returns the squared values in a new array sorted in descending order. The function should have a time complexity of O(nlogn) and a space complexity of O(n), where n is the length of the input array.
"""

def square_and_sort(arr):
    return sorted([abs(num) ** 2 for num in arr], reverse=True)
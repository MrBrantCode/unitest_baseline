"""
QUESTION:
Write a function named `count_occurrences` that takes an array of integers and an integer value as parameters. The function must return the number of occurrences of the given value in the array with a time complexity of O(n) and a space complexity of O(1).
"""

def count_occurrences(arr, value):
    count = 0
    for num in arr:
        if num == value:
            count += 1
    return count
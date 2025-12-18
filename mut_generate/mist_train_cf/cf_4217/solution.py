"""
QUESTION:
Create a function `count_occurrence` that takes an array and a target number as input. The function should return the number of occurrences of the target number in the array. The solution must have a time complexity of O(n), where n is the length of the array, and cannot use any additional data structures, loops, built-in functions, or recursion directly to count the occurrences.
"""

def count_occurrence(arr, num):
    if len(arr) == 0:
        return 0
    return (arr[0] == num) + count_occurrence(arr[1:], num)
"""
QUESTION:
Write a function named `find_second_highest_odd` that takes an array of integers as input and returns the second highest odd value in the array. If the array has less than two elements or there is no odd value in the array, return -1. The solution must have a time complexity of O(nlogn) and a space complexity of O(1), and it should be implemented using a recursive approach without modifying the original array.
"""

def find_second_highest_odd(arr):
    if len(arr) < 2:
        return -1
    
    return find_second_highest_odd_recursive(arr, -1, -1)

def find_second_highest_odd_recursive(arr, highest, second_highest):
    if len(arr) == 0:
        return second_highest
    
    num = arr.pop()
    
    if num % 2 != 0:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num
    
    return find_second_highest_odd_recursive(arr, highest, second_highest)
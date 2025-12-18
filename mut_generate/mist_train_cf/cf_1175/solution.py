"""
QUESTION:
Write a function named `find_second_highest_odd` that finds the second highest odd value in a given array. The function should return the second highest odd value if it exists; otherwise, return -1. The time complexity should be O(nlogn) and the space complexity should be O(1). The solution should not modify the original array.
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
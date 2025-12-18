"""
QUESTION:
Implement a function `print_reverse(array, index=0)` that prints each element of a given array in reverse order. The function must not use any additional data structures, modify the original array, or utilize built-in reverse functions. The time complexity should be O(n) and the space complexity should be O(1).
"""

def print_reverse(array, index=0):
    if index == len(array):
        return
    print_reverse(array, index+1)
    print(array[len(array)-index-1])
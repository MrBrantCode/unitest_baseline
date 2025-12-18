"""
QUESTION:
Write a function `find_largest` that takes an array of integers as input and returns the largest number in the array. The array can contain both positive and negative integers. The function should use only basic arithmetic operations and control structures, without relying on any built-in functions or methods. The time complexity of the solution should be O(n), where n is the length of the array.
"""

def find_largest(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num
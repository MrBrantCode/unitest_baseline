"""
QUESTION:
Write a function named `find_largest_number` that takes an array of real numbers as input, where the length of the array is at least one. The function should return the largest number in the array. The time complexity should be O(n) and the space complexity should be O(1), where n is the number of elements in the array.
"""

def find_largest_number(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num
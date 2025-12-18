"""
QUESTION:
Write a function `find_third_largest(arr)` that finds the third largest distinct number in an array of integers without using any built-in sorting functions or additional data structures. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def find_third_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    third_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            third_largest = second_largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            third_largest = second_largest
            second_largest = num
        elif num > third_largest and num != largest and num != second_largest:
            third_largest = num
    
    return third_largest
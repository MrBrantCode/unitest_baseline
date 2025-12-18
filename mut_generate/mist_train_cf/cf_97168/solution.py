"""
QUESTION:
Write a function named `find_second_largest` that takes an array of integers as input and returns the element with the second greatest value. The function should not use any built-in sorting functions or methods and should have a time complexity of O(n), where n is the length of the array. The input array contains at least 2 unique integers.
"""

def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    return second_largest
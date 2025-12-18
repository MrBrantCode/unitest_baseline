"""
QUESTION:
Write a function named `largest_numbers` that takes an array of integers as input and returns a list of the two largest numbers in the array in reverse order (i.e., the largest number first). The input array may contain duplicate numbers.
"""

def largest_numbers(array):
    largest = float('-inf')
    second_largest = float('-inf')
    for i in array:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return [largest, second_largest]
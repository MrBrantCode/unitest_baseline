"""
QUESTION:
Write a function named `find_third_smallest` that takes an array of positive integers as input, where the array size is between 10 and 100 (inclusive), and returns the third smallest unique element in the array. The array may contain duplicate elements.
"""

def find_third_smallest(arr):
    smallest = float('inf')
    second_smallest = float('inf')
    third_smallest = float('inf')
    
    for num in arr:
        if num < smallest:
            third_smallest = second_smallest
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            third_smallest = second_smallest
            second_smallest = num
        elif second_smallest < num < third_smallest:
            third_smallest = num
    
    return third_smallest
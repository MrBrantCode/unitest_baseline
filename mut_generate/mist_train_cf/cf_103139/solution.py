"""
QUESTION:
Create a function named `findSecondSmallest(arr)` that takes an array of integers as input and returns the second smallest element. If the array has less than two unique elements, the function can return any value or throw an exception, as this case is not specified. The array may contain duplicate elements.
"""

def findSecondSmallest(arr):
    smallest = float('inf')
    secondSmallest = float('inf')
    
    for num in arr:
        if num < smallest:
            secondSmallest = smallest
            smallest = num
        elif num > smallest and num < secondSmallest:
            secondSmallest = num
            
    return secondSmallest
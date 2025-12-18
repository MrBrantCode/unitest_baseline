"""
QUESTION:
Write a function `findSecondThirdMin` that takes a list of integers as input and returns a list containing the second and third smallest unique integers in ascending order. The function should have a time complexity better than O(n^2) and handle duplicate values and edge cases where there are less than three unique integers in the input list.
"""

def findSecondThirdMin(arr):
    unique_nums = list(set(arr)) # Removing duplicate values
    first_min, second_min, third_min = float('inf'), float('inf'), float('inf')

    for num in unique_nums:
        if num <= first_min:
            third_min = second_min
            second_min = first_min
            first_min = num
        elif num <= second_min:
            third_min = second_min
            second_min = num
        elif num <= third_min:
            third_min = num     

    if second_min == float('inf') or third_min == float('inf'):
        return None 

    return [second_min, third_min]
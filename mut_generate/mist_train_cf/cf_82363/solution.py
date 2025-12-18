"""
QUESTION:
Write a function `penultimate_max(arr)` that finds the second highest value in an unordered list of distinct integers without using any pre-existing Python libraries or built-in functions for sorting or maximum value determination. The function should return `None` if the list has less than two elements.
"""

def penultimate_max(arr):
    if len(arr) < 2:
        return None  # If the list has less than two elements, there is no penultimate max
    max1, max2 = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
  
    for num in arr[2:]:
        if num > max1:
            max1, max2 = num, max1  # If number is greater than max1, update max1 and demote max1 to max2
        elif num > max2:
            max2 = num  # If number is not higher than max1 but higher than max2, then update max2
    return max2
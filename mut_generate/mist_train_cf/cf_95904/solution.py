"""
QUESTION:
Write a function named `find_largest_negative` that takes an array of integers as input and returns the largest negative number if the array contains all negative numbers and does not contain any duplicate elements. If the array is empty, return "Array is empty." If the array contains at least one non-negative number, return the largest non-negative number. If the array contains duplicate negative elements, consider only one occurrence of each element. The function should not use any built-in sorting or max functions and should run in O(n) time complexity.
"""

def find_largest_negative(arr):
    if len(arr) == 0:
        return "Array is empty."

    has_positive = False
    has_duplicates = False
    largest_negative = float('-inf')  
    seen = set()

    for num in arr:
        if num >= 0:
            has_positive = True
            continue
        elif num in seen:
            has_duplicates = True
        else:
            seen.add(num)
            if num > largest_negative:
                largest_negative = num

    if has_duplicates:
        for num in seen:
            if num > largest_negative:
                largest_negative = num
    elif has_positive:
        return max(arr)

    if largest_negative == float('-inf'):
        return max(arr) if has_positive else "No negative numbers found."
    else:
        return largest_negative
"""
QUESTION:
Create a function `find_final_position` that takes two parameters: an array of integers and a target integer. The function should return the position of the final appearance of the target integer in the array. If the target integer is not found in the array, return "Integer not found in array". Note that the position should be zero-based.
"""

def find_final_position(arr, target):
    if target in arr:
        return len(arr) - 1 - arr[::-1].index(target)
    else:
        return "Integer not found in array"
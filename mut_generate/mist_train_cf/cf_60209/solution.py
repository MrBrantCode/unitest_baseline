"""
QUESTION:
Write a function `get_middle_elements` that takes an array as input and returns the middle 3 elements. If the array size is even and greater than or equal to 4, the function should return the two middle numbers. If the array size is less than 3, the function should return "Insufficient elements". The function should have optimal time complexity.
"""

def get_middle_elements(arr):
    size = len(arr)
    if size < 3:
        return "Insufficient elements"
    elif size % 2 == 0:
        return arr[size//2-1:size//2+1]
    else:
        return arr[size//2-1:size//2+2]
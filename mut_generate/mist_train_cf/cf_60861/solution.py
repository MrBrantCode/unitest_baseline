"""
QUESTION:
Design a function `first_five_mirrored` that takes an array as input, returns the first five elements of the array in mirrored sequence, and appends the mirrored elements after the original first five elements. The array has at least five elements. The mirrored sequence should be in the format of ABCDE EDCBA.
"""

def first_five_mirrored(arr):
    # Get first 5 elements
    first_five = arr[:5]
    # Return mirrored sequence
    return first_five + first_five[::-1]
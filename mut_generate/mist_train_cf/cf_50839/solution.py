"""
QUESTION:
Write a function named `solve` that takes an array of strings as input, where each string contains only lowercase letters. The function should return the array rearranged based on the length of each string in ascending order, with each string reversed. The input array should not be modified, and any non-alphabetic characters should be ignored.
"""

def solve(arr):
    # Clean the array first
    clean_arr = ["".join(filter(str.isalpha, item.lower())) for item in arr]
    # Sort the array based on string length and reverse each string
    return sorted([item[::-1] for item in clean_arr], key=len)
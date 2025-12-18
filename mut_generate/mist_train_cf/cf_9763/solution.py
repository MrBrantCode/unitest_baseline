"""
QUESTION:
Convert a 12-element array of integers ranging from -100 to 355 to a string representation. The input array should be [105, -152, 85, 255, 0, 256, -88, 88, 105, 133, 233, 240]. Implement a function named array_to_string to solve this problem.
"""

def array_to_string(arr):
    return ", ".join(str(num) for num in arr)
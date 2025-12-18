"""
QUESTION:
Create a function named `smallest_alphanumeric` that takes an array of mixed type elements as input and returns the smallest alphanumeric string. The smallest alphanumeric string is determined by sorting the alphanumeric elements in ascending/alphabetical order. The input array may contain non-alphanumeric elements, which should be excluded from the comparison.
"""

def smallest_alphanumeric(arr):
    alphanumeric_arr = [str(i) for i in arr if str(i).isalnum()] 
    alphanumeric_arr.sort()
    return alphanumeric_arr[0]
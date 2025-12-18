"""
QUESTION:
Create a function named `sort_alphanumeric` that takes an array of alphanumeric strings as input and returns the sorted array in ascending order based on the numerical value of each string. The numerical value is obtained by extracting the digits from each string and converting them to an integer.
"""

def sort_alphanumeric(arr):
    return sorted(arr, key=lambda x: int(''.join(filter(str.isdigit, x))))
"""
QUESTION:
Create a function called `find_least_occurrence` that takes an array of floating point numbers as input and returns the number that appears with the smallest frequency. If there are multiple numbers with the same smallest frequency, any one of them can be returned.
"""

def find_least_occurrence(arr):
    # Create a dictionary to store numbers and their occurrence
    num_dict = {}
    for num in arr:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    # Get the number with smallest occurrence
    least_occurrence = min(num_dict.values())
    for key in num_dict:
        if num_dict[key] == least_occurrence:
            return key
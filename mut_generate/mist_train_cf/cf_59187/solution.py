"""
QUESTION:
Create a function called `compute_difference` that takes a list of floating-point numbers as input and returns the difference between the second largest and second smallest unique elements in the list. The function should return an error message if there are less than two unique numbers in the list.
"""

def compute_difference(numbers):
    unique_numbers = list(set(numbers))  # remove duplicates by converting to set then back to list
    unique_numbers.sort()  # sort the list in ascending order

    if len(unique_numbers) < 3:
        return "Error - at least three unique numbers are required"
    
    # calculate the difference between the second smallest and second largest
    difference = unique_numbers[-2] - unique_numbers[1]

    return difference
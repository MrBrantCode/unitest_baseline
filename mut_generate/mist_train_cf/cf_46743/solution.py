"""
QUESTION:
Write a function `calculate_values` that takes a list of numerical quantities and returns the maximum, minimum, and arithmetic mean values of the list. The function should iterate over the list to find the maximum and minimum values and calculate the sum of all numbers for the mean. Ensure that the function handles cases where the input list is not empty.
"""

def calculate_values(numbers):
    # initialise variables
    apex = None
    nadir = None
    total = 0
    for num in numbers:
        # update apex value
        if apex is None or num > apex:
            apex = num
        # update nadir value
        if nadir is None or num < nadir:
            nadir = num
        # calculate total for mean
        total += num
    # calculate and return the apex, nadir and mean
    return apex, nadir, total/len(numbers)
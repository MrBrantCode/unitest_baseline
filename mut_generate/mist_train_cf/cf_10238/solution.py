"""
QUESTION:
Write a function named `average_above_five` that takes a list of integers as input and returns the average of the integers greater than 5. The function should return 0 if there are no integers greater than 5 in the list.
"""

def average_above_five(lst):
    # Filter the list for integers greater than 5
    above_five = [num for num in lst if num > 5]
    
    # If no integers are greater than 5, return 0
    if len(above_five) == 0:
        return 0
    
    # Calculate the average of the integers greater than 5
    return sum(above_five) / len(above_five)
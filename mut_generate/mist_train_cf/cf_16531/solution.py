"""
QUESTION:
Write a function `calculate_average` that calculates the average of a list of numbers, considering duplicates, and rounds it to the nearest integer. The input list can contain up to 1 million elements. The function should take a list of numbers as input and return the rounded average as an integer.
"""

def calculate_average(a_list):
    # Calculate the sum of all elements in the list
    total_sum = sum(a_list)
    
    # Count the number of elements in the list
    count = len(a_list)
    
    # Calculate the average by dividing the sum by the count
    average = total_sum / count
    
    # Round the average to the nearest integer
    rounded_average = round(average)
    
    return rounded_average
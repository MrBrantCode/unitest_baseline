"""
QUESTION:
Write a function named `calculate_average` that calculates the average of an array of integers. The array may be empty and can contain any number of elements. The function should return the calculated average. If the array is empty, it should return 0.
"""

def calculate_average(array):
    if not array:
        return 0
    
    total_sum = sum(array)
    average = total_sum / len(array)
    
    return average
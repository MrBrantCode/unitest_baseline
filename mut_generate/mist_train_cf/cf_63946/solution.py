"""
QUESTION:
Create a function named `weighted_average` that takes two lists of equal length as input: a list of whole numbers and a list of their corresponding weights. The function should calculate and return the weighted arithmetic average of the numbers. If the input lists are not of equal length, the function should return an error message.
"""

def weighted_average(numbers, weights):
    if len(numbers) != len(weights):
        return 'Error: Lists must be of equal length.'
    
    total = 0
    weight_sum = 0
    
    for i in range(len(numbers)):
        total += numbers[i] * weights[i]
        weight_sum += weights[i]
    
    return total / weight_sum
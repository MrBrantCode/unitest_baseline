"""
QUESTION:
Write a function `top_three_highest_and_lowest` that takes an array of numbers as input and returns a dictionary with two keys: 'highest' and 'lowest'. The 'highest' key maps to a list of the top three highest numbers in the array, and the 'lowest' key maps to a list of the lowest three numbers in the array. The function should only consider distinct values and should handle the case where the array has less than three elements, returning an error message in this case.
"""

def top_three_highest_and_lowest(arr):
    if len(arr) < 3:
        return 'The array should have at least 3 elements'

    highest = [float('-inf'), float('-inf'), float('-inf')]
    lowest = [float('inf'), float('inf'), float('inf')]

    for num in arr:
        # Check and update the highest values
        if num > highest[0]:
            highest[2] = highest[1]
            highest[1] = highest[0]
            highest[0] = num
        elif num > highest[1]:
            highest[2] = highest[1]
            highest[1] = num
        elif num > highest[2]:
            highest[2] = num

        # Check and update the lowest values:
        if num < lowest[0]:
            lowest[2] = lowest[1]
            lowest[1] = lowest[0]
            lowest[0] = num
        elif num < lowest[1]:
            lowest[2] = lowest[1]
            lowest[1] = num
        elif num < lowest[2]:
            lowest[2] = num
    
    return {
        'highest': sorted(highest, reverse=True),
        'lowest': sorted(lowest)
    }
"""
QUESTION:
Create a function named `sum_and_identify` that takes an array of numbers as input. The function should return two values: a list of sums of each successive pair of numbers in the array, and a list of pairs where the difference between the two numbers exceeds 1.
"""

def sum_and_identify(arr):
    pairs = [(arr[i], arr[i+1]) for i in range(len(arr)-1)]
    sums = [sum(pair) for pair in pairs]
    diff_over_one = [pair for pair in pairs if abs(pair[0]-pair[1]) > 1]
    
    return sums, diff_over_one
"""
QUESTION:
Design a function named "calculate_cumulative" that takes an array of numbers as input and returns a list of tuples. Each tuple should contain a pair of successive numbers from the array, their cumulative sum, and a boolean flag indicating whether the absolute difference between the pair of numbers is greater than 1. The function should process each pair of successive numbers in the input array exactly once.
"""

def calculate_cumulative(arr):
    result = []
    for i in range(len(arr)-1):
        pair = (arr[i], arr[i+1])
        cum_sum = sum(pair)
        variance = abs(pair[0] - pair[1])
        flag = variance > 1
        result.append((pair, cum_sum, flag))
    return result
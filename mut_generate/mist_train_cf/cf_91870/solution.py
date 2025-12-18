"""
QUESTION:
Write a function named `mean(arr)` that takes an array of integers as input and returns the mean of the integers. The function must have a time complexity of O(n), where n is the number of integers in the array, and a space complexity of O(1). Do not use any built-in functions or libraries to calculate the mean.
"""

def mean(arr):
    sum = 0
    count = 0
    
    for num in arr:
        sum += num
        count += 1
    
    mean = sum / count
    return mean
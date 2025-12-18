"""
QUESTION:
Write a function named `mean` that calculates the mean of an array of integers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of integers in the array. The input array can contain up to 10^6 integers. Do not use any built-in functions or libraries to calculate the mean. The function should return the calculated mean.
"""

def calculate_mean(arr):
    sum = 0
    count = 0
    
    for num in arr:
        sum += num
        count += 1
    
    mean = sum / count
    return mean
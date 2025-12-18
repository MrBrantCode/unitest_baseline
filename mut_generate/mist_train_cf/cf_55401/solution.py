"""
QUESTION:
Create a function `calculate_sum` that takes an array of integers as an argument and returns the sum of all the elements in the array. The function should iterate through the array and add each element to the total sum. The function should not use the built-in `sum` function in Python.
"""

def calculate_sum(arr):
    total = 0  
    for i in arr:
        total += i  
    return total  
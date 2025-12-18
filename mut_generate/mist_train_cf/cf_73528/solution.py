"""
QUESTION:
Define a function named `increment_final_component` that takes an array of numbers as input. The function should increment the last element of the array by 10, but if the result exceeds 100, it should reset the last element to its original value instead.
"""

def increment_final_component(arr):
    if arr[-1] + 10 > 100:
        return arr
    else:
        arr[-1] += 10
        return arr
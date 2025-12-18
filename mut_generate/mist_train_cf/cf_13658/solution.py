"""
QUESTION:
Create a function `top_n_elements` that takes two parameters: an array of integers and an integer `n`. The function should return a list of the top `n` highest valued elements in the array in descending order.
"""

def top_n_elements(arr, n):
    sorted_arr = sorted(arr, reverse=True)  # Sort the array in descending order
    return sorted_arr[:n]  # Return the first n elements of the sorted array
"""
QUESTION:
Create a function called `find_top_n` that takes two parameters: an array of integers and an integer `n`. The function should return the top `n` highest valued elements in the array in descending order. The function should return the elements in the order of their values from highest to lowest.
"""

def find_top_n(arr, n):
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[:n]
"""
QUESTION:
Create a function called `remove_divisible_elements` that takes an array of integers as input, removes elements that are both divisible by 5 and greater than 10, and returns the remaining elements in descending order.
"""

def remove_divisible_elements(arr):
    filtered_arr = [x for x in arr if x <= 10 or x % 5 != 0]
    filtered_arr.sort(reverse=True)
    return filtered_arr